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


setup(setup_requires=['pbr'],
      pbr=True,
      )
