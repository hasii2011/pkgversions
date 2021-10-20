import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pkgversions",
    version="0.2.1",
    author_email='Humberto.A.Sanchez.II@gmail.com',
    description='A build help tool',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hasii2011/pkgversions",
    packages=[
        'pkgversions',
        'pkgversions.resources'
    ],
    package_data={'pkgversions.resources': ['loggingConfiguration.json', 'loggingConfiguration.json']},
    include_package_data=True,
    install_requires=['click'],
    entry_points={
        'console_scripts': ['pkgversions=pkgversions.PkgVersions:commandHandler']
    }
)
