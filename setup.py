from distutils.core import setup
import re
from os.path import join, dirname


__file_path = dirname(__file__)
version = '0.1.4'
module_name = 'get_media_files'
github_url = 'https://github.com/jtara1/{}'.format(module_name)
with open(join(__file_path, 'README.rst')) as f:
    readme = f.read()


def get_install_requirements():
    requirements = []
    try:
        with open(join(__file_path, 'requirements.txt'), 'r') as req_file:
            for line in req_file:
                requirements.append(re.sub("\s", "", line))
    except (FileExistsError, FileNotFoundError):
        pass
    return requirements


setup(name=module_name,
      packages=[module_name],
      version=version,
      description='Wrapper for pymediainfo that retrieves information such as'
                  'media type, duration, resolution, etc. from media files',
      long_description=readme,
      author='James T',
      author_email='jtara@tuta.io',
      url=github_url,
      download_url='{github_url}/archive/{version}.tar.gz'
      .format(github_url=github_url, version=version),
      keywords=['pymediainfo', 'wrapper', 'get media files', 'info'],
      install_requires=get_install_requirements(),
      classifiers=['Programming Language :: Python :: 3.5',
                   'Environment :: Console',
                   'Intended Audience :: Developers']
      )
