import sys
from os.path import join, dirname, abspath
__file_path = dirname(__file__)
sys.path.append(join(__file_path, '..'))

from get_media_files import GetMediaFiles


media_dir = join(__file_path, 'media')
media = GetMediaFiles(media_dir)  # GetMediaFiles object


def test_data():
    print(media)

    expected_data = [
        [abspath('tests/media/about.txt'),
         {'General': {'duration': None, 'format': None, 'size': (None, None)}},
         1513722595.3195267],
        [abspath('tests/media/044838940-mountain-range-and-lake-2006-a.jpg'),
         {'General': {'duration': None, 'format': 'JPEG',
                      'size': (None, None)},
          'Image': {'duration': None, 'format': 'JPEG', 'size': (800, 536)}},
         1513722595.3235266],
        [abspath('tests/media/044837513-two-women-walking-hill-1930s-v.jpg'),
         {'General': {'duration': None, 'format': 'JPEG',
                      'size': (None, None)},
          'Image': {'duration': None, 'format': 'JPEG', 'size': (1024, 772)}},
         1513722595.3275266],
        [abspath('tests/media/045844231-my-mother.wav'),
         {'Audio': {'duration': 12863, 'format': 'PCM', 'size': (None, None)},
          'General': {'duration': 12863, 'format': 'Wave',
                      'size': (None, None)}},
         1513722595.3315265]
    ]
    assert(expected_data == media.files)


def test_length():
    assert(len(media) == 4)


def test_data_of_individual_file():
    expected_data = [
        [abspath('tests/media/044837513-two-women-walking-hill-1930s-v.jpg'),
         {'General': {'size': (None, None),
                      'format': 'JPEG', 'duration': None},
          'Image': {'size': (1024, 772), 'format': 'JPEG', 'duration': None}},
         1513722595.3275266]
    ]

    media_file = join(media_dir,
                      '044837513-two-women-walking-hill-1930s-v.jpg')
    media2 = GetMediaFiles(media_file)
    assert(media2.get_info() == expected_data)


if __name__ == '__main__':
    test_data()
