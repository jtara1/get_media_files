from distutils.core import setup
import re


version = '0.1.1'


def get_install_requirements():
    requirements = []
    with open('requirements.txt', 'r') as f:
        for line in f:
            requirements.append(re.sub("\s", "", line))
    print(requirements)
    return requirements


if __name__ == "__main__":
    pass


setup(name='get_media_files',
      packages=['get_media_files'],
      version=version,
      description='Wrapper for pymediainfo that retrieves information such as'
                  'media type, duration, resolution, etc. from media files',
      author='James T',
      author_email='jtara@tuta.io',
      url='https://github.com/jtara1/get_media_info',
      download_url='https://github.com/jtara1/get_media_files/archive/{version}.tar.gz'
      .format(version=version),
      keywords=['pymediainfo', 'wrapper', 'get media files', 'info', 'duration'],
      install_requires=get_install_requirements(),
      classifiers=[]
      )
