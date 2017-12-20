import sys
from os.path import join, dirname
__file_path = dirname(__file__)
sys.path.append(join(__file_path, '..'))

from get_media_files import GetMediaFiles


media_dir = join(__file_path, 'media')


def test():
    expected_data = [
     ['tests/media/about.txt',
      {'General': {'duration': None, 'format': None, 'size': (None, None)}},
      1513722595.3195267],
     ['tests/media/044838940-mountain-range-and-lake-2006-a.jpg',
      {'General': {'duration': None, 'format': 'JPEG', 'size': (None, None)},
       'Image': {'duration': None, 'format': 'JPEG', 'size': (800, 536)}},
      1513722595.3235266],
     ['tests/media/044837513-two-women-walking-hill-1930s-v.jpg',
      {'General': {'duration': None, 'format': 'JPEG', 'size': (None, None)},
       'Image': {'duration': None, 'format': 'JPEG', 'size': (1024, 772)}},
      1513722595.3275266],
     ['tests/media/045844231-my-mother.wav',
      {'Audio': {'duration': 12863, 'format': 'PCM', 'size': (None, None)},
       'General': {'duration': 12863, 'format': 'Wave', 'size': (None, None)}},
      1513722595.3315265]
    ]
    media = GetMediaFiles(media_dir)
    print(media)
    assert(expected_data == media.files)


if __name__ == '__main__':
    test()
