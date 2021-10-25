[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pkgversions.svg)](https://badge.fury.io/py/pkgversions)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

##Introduction
This is a simple CLI for me to update package versions during development.
This command has to be run solely during development and in the virtual environment of the 
target py2app application.

##How to use
```commandline
pkgversions --help
Usage: pkgversions [OPTIONS]

  For best results install this command in the virtual environment that
  contains the packages that you intend to query

Options:
  -p, --package-file PATH   location of packages list file
  -o, --versions-file PATH  location of generated versions file
  --version                 Show the version and exit.
  --help                    Show this message and exit.
```
