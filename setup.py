from setuptools import setup, find_packages
import io, os

# This setup file is based on https://github.com/a2e-mmc/mmctools/blob/master/setup.py

NAME = 'wetools'
DESCRIPTION = 'Collection of pre- and post-processing tools for wind energy research'
URL = 'https://github.com/rthedin/wetools'
EMAIL = 'registhedin@gmail.com'
AUTHOR = ''
REQUIRES_PYTHON = '>=3.10.5'
VERSION = '0.0.1'


REQUIRED = [
    'matplotlib>=3.5.3',
    'numpy>=1.23.2',
    'scipy>=1.9.0',
    'pandas>=1.4.3',
    'xarray>=2022.6.0',
    'netcdf4>=1.6.0',
    'dask>=2022.8.1',
]

EXTRAS = {}

currpath = os.path.abspath(os.path.dirname(__file__))
# Get long description from README
try:
    with io.open(os.path.join(currpath, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(currpath, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION



setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=[NAME],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
)

