import re
import os
import glob
from operator import itemgetter
from pymediainfo import MediaInfo
import time
import click
from pprint import pformat


class GetMediaFiles:
    media_info_dll_location = "C:\\Program Files\\MediaInfo\\MediaInfo.dll"

    def __init__(self, path=os.path.dirname(os.path.abspath(__file__)),
                 track_types=('Video', 'Audio', 'Image', 'General')):
        """Returns sorted list of files from param path
        
        :param path: the path containing file(s)
        :param track_types: tuple or list of strings of the file types we
            want to get information on; only valid strings are 'Video', 
            'Audio', 'Image', 'General' 
        """
        self.files = None  # list containing information on files
        self.path = path
        # Any file with one of the follow MediaInfo "tracks" will be returned
        self.track_types = track_types if track_types \
            else ['Image', 'Video', 'Audio']
        self.get_info()

    def get_info(self, path=None, recursive=False,
                 track_types=None, sort='st_ctime', sort_reverse=False,
                 start_i=0, limit_i=-1, remove_audio=False):
        """Utilize pymediainfo to get media tracks, size, duration, & format
        Returns a list of lists with file info (see readme.md for more details)

        :param path: folder path containing media files
        :param recursive: get files inside of folders inside of folders ...
        :param track_types: list containg 'Image' or 'Video' or 'Audio' or 
            'General'
        :param sort: os.stat(path) returns a tuple, access value 
            from that tuple with sort param
        :param sort_reverse: Reverse after sorting
        :param start_i: start index to begin getting files at
        :param limit_i: end index to stop getting files before
        :param remove_audio: removes files that are audio only if True 
            (redundant)
        """
        path = path if path else self.path
        track_types = track_types if track_types else self.track_types
        # debug
        print('[get_media_files] Getting files with %s in %s'
              % (track_types, path))

        # get all files (and directories) in path
        files = glob.glob(os.path.join(path, '**'), recursive=recursive)
        limit_i = len(files) if limit_i == -1 else limit_i
        files = files[start_i:limit_i]

        # reorganize so we can append data with each file
        files = list([f] for f in files)

        # e.g.: '(Audio|Video|Image)'
        media_types = '|'.join(track_types)
        media_type_regex = re.compile('(' + media_types + ')')

        # Note: every file seems to have at least one track ('General')
        remove_indices = []
        for f in files:
            # get Media Info of current file
            try:
                info = MediaInfo.parse(f[0])
            except OSError:
                info = MediaInfo.parse(
                    f[0],
                    library_file=GetMediaFiles.media_info_dll_location
                )

            # append track info if it matches that given by track_types
            f.append({track.track_type: {
                        'size': (track.width, track.height),
                        'format': track.format,
                        'duration': track.duration
                        }
                        for track in info.tracks
                        if re.match(media_type_regex, str(track.track_type))
                     })

            # remove if folder, non media, or audio
            if (len(f) == 1 or f[1] == {}) or \
                    (remove_audio and 'Audio' in f[1].keys() and len(f) == 2):

                remove_indices.append(files.index(f))
                continue

        # remove unwanted files in files list
        for count, index in enumerate(remove_indices):
            files.remove(files[index - count])

        # return if we don't care about sorting by creation date or
        # attaching creation date data
        if not sort:
            return files

        # attach stats (mutates files) then sort files
        self.files = files
        self._attach_stats(stat_type=sort)
        self.files = sorted(files, key=itemgetter(-1), reverse=sort_reverse)

        return self.files

    def _get_stats(self, stat_type='st_ctime'):
        """Valid stat_type params
        https://docs.python.org/3/library/os.html#os.stat_result
        """
        if self.files is None:
            print("[get_media_files] Warning: attempted to get_stats before"
                  " method get_info was called")
            return []
        return list(getattr(os.stat(f[0]), stat_type) for f in self.files)

    def _attach_stats(self, stat_type='st_ctime'):
        """Mutate files with os.stat(path).stat_type"""
        stats = self._get_stats(stat_type=stat_type)
        self.files = list(f.append(stat) for f, stat in zip(self.files, stats))

    def __str__(self):
        if self.files is None:
            print("[get_media_files] Warning: attempted to print before"
                  " method get_info was called")
            return "[]"
        return pformat(self.files)


if __name__ == "__main__":
    init_t = time.time()

    @click.command()
    @click.argument('folder')
    @click.option('-r', '--recursive', default=False)
    @click.option('-t', '--track-types', default=['Image', 'Video', 'Audio'])
    def main(folder, recursive, track_types):
        media = GetMediaFiles(path=folder, track_types=track_types)
        files = media.get_info(recursive=recursive, sort='st_ctime',
                               start_i=0, limit_i=-1)
        print('----------------------------')
        print('%s files found.' % len(files))
        print('%i seconds passed' % int(time.time() - init_t))
        print(media)

    main()
