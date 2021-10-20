
from typing import TextIO

import logging

from logging import Logger
from logging import getLogger
from logging import config

from os import sep as osSep
from os import linesep as osLineSep

from json import load as jsonLoad

from click import command
from click import option
from click import style

from click import Path as clickPath
from click import clear as clickClear
from click import echo as clickEcho
from click import version_option
from click import open_file


from pkg_resources import resource_filename
from pkg_resources import get_distribution


class PkgVersions:

    JSON_LOGGING_CONFIG_FILENAME: str = "loggingConfiguration.json"
    MADE_UP_PRETTY_MAIN_NAME:     str = "PkgVersionsCli"

    RESOURCES_PACKAGE_NAME: str = 'pkgversions.resources'
    RESOURCES_PATH:         str = f'pkgversions{osSep}resources'
    RESOURCE_ENV_VAR:       str = 'RESOURCEPATH'

    def __init__(self, packageFile: clickPath, versionsFile: clickPath):

        self._setupSystemLogging()
        self.logger: Logger = getLogger(PkgVersions.MADE_UP_PRETTY_MAIN_NAME)

        self._packageFile:  clickPath = packageFile
        self._versionsFile: clickPath = versionsFile

    def generateVersions(self):

        readDescriptor:  TextIO = open_file(self._packageFile,  mode='r')
        writeDescriptor: TextIO = open_file(self._versionsFile, mode='w')

        packageName: str = readDescriptor.readline()
        while packageName:
            pkgVersion: str = get_distribution(packageName).version

            packageName = packageName.rstrip(f'{osLineSep}')
            versionLine: str = f"{packageName}={pkgVersion}"
            self.logger.info(f'{versionLine=}')
            writeDescriptor.write(f'{versionLine}{osLineSep}')
            packageName = readDescriptor.readline()

        readDescriptor.close()
        writeDescriptor.close()

    def _setupSystemLogging(self):
        configFilePath: str = self._retrieveResourcePath(PkgVersions.JSON_LOGGING_CONFIG_FILENAME)

        with open(configFilePath, 'r') as loggingConfigurationFile:
            configurationDictionary = jsonLoad(loggingConfigurationFile)

        config.dictConfig(configurationDictionary)
        logging.logProcesses = False
        logging.logThreads   = False

    def _retrieveResourcePath(self, bareFileName: str) -> str:

        # Use this method in Python 3.9
        # from importlib_resources import files
        # configFilePath: str  = files('travisci.resources').joinpath(TravisCli.JSON_LOGGING_CONFIG_FILENAME)

        try:
            fqFileName: str = resource_filename(PkgVersions.RESOURCES_PACKAGE_NAME, bareFileName)
        except (ValueError, Exception):
            #
            # Maybe we are in an app
            #
            from os import environ
            pathToResources: str = environ.get(f'{PkgVersions.RESOURCE_ENV_VAR}')
            fqFileName:      str = f'{pathToResources}{osSep}{PkgVersions.RESOURCES_PATH}{osSep}{bareFileName}'

        return fqFileName

    def retrieveResourceText(self, bareFileName: str) -> str:
        """
        Get text out of file

        Args:
            bareFileName:

        Returns:  A long string
        """
        textFileName: str = self._retrieveResourcePath(bareFileName)
        self.logger.debug(f'{textFileName=}')

        objRead = open(textFileName, 'r')
        requestedText: str = objRead.read()
        objRead.close()

        return requestedText


@command()
@option('-p', '--package-file',  required=False, default='pkgversions/resources/packages.txt', type=clickPath(exists=True),  help='location of packages list file')
@option('-o', '--versions-file', required=False, default='pkgversions/resources/versions.txt', type=clickPath(exists=False), help='location of generated versions file')
@version_option(version='0.2.1', message='%(version)s')
def commandHandler(package_file: clickPath, versions_file: clickPath):
    """
    For best results install this command in the virtual environment that contains the packages that
    you intend to query
    """

    clickClear()
    clickEcho(style(f"Starting {PkgVersions.MADE_UP_PRETTY_MAIN_NAME}", reverse=True))

    pkgVersions: PkgVersions = PkgVersions(packageFile=package_file, versionsFile=versions_file)

    pkgVersions.generateVersions()


if __name__ == "__main__":

    commandHandler()
