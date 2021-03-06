from os import path
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
ipchange does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='ipchange',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="IP Change Scripts for NSLS-II Devices",
    long_description=readme,
    author="Brookhaven National Lab",
    author_email='swilkins@bnl.gov',
    url='https://github.com/NSLS-II/ipchange',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'moxa_change_ip = ipchange.moxa.cmd:moxa_change_ip',
            'moxa_change_passwd = ipchange.moxa.cmd:moxa_change_passwd',
            'moxa_download = ipchange.moxa.cmd:moxa_download',
            'axis_change_ip = ipchange.axis.cmd:axis_change_ip',
            'axis_change_passwd = ipchange.axis.cmd:axis_change_passwd',
            'hiden_change_ip = ipchange.hiden.cmd:hiden_change_ip',
        ],
    },
    include_package_data=True,
    package_data={
        'ipchange': [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
