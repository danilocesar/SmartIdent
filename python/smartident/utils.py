import sys
import os
from enum import Enum
from clang import ClangFormatLocator
from makefile import MakeFileHandler
from smartparser import SmartParser

SPACE = 1
TAB = 2

class FileType(Enum):
    MAKEFILE = 1
    CSOURCE = 2
    CHEADER = 3
    UNKNOWN = 256

class SmartFileHandle:
    """ SmartFileHandle

    This class should do the hard work of read the file,
    define its type, etc...
    """

    def __init__(self, url):

        self.__fullpath = os.path.abspath(url)
        self.__filename = os.path.basename(url);
        self.__dirname = os.path.dirname(self.__fullpath)

        self.__type = self.__detect_type()

        if self.__type == FileType.MAKEFILE:
            self.__makefileHandler = MakeFileHandler()
            self.__rules = self.__makefileHandler.getRules()
            return

        if self.__type in [FileType.CSOURCE, FileType.CHEADER]:
            self.__clangLocator = ClangFormatLocator(self.__dirname)

            # In case there's a .clang-format, get the rules and leave
            if self.__clangLocator.searchAndReadClangFormatFile():
                self.__rules = self.__clangLocator.getRules()
                return

            # TODO: Implement a check for vim direct instructions

            self.__smartParser = SmarParser(self.__fullpath)
            self.__rules = self.__smartParser.getRules()

    def getRules(self):
        return self.__rules

    def getType(self):
        """ Get the detected file type """
        return self.__type

    def __detect_type(self):
        """
        As a first version, detecting the file type via filename should be enough.
        """

        # TODO: Perhaps we should use Mimetypes in the future

        if self.__filename in ["Makefile", "GNUMakefile"]:
            return FileType.MAKEFILE

        elif self.__filename.endswith(".c") or self.__filename.endswith(".cpp"):
            return FileType.CSOURCE

        elif self.__filename.endswith(".h") or  self.__filename.endswith(".hpp"):
            return FileType.CHEADER

        return FileType.UNKNOWN
        pass



def processFile(filename):
    spaces = {}
    tabs = 0
    lines = 0
    with open(filename, 'rb', 1024*1024) as f:
        for line in f:
            # break in case we don't find line starting with space or tab
            if not (line.startswith(' ') or line.startswith('\t')):
                continue

            # count spaced lines
            lines += 1

            # ignore comments
            stripedline = line.strip()
            if stripedline.startswith('//') or \
                stripedline.startswith('/*') or \
                stripedline.startswith('*') or \
                stripedline.startswith('#') or \
                stripedline.startswith("\""):
                continue

            # ignore empty lines
            if len(stripedline) == 0:
                continue

            chars, linetype = count_spaces(line)
            if linetype == SPACE:
                if not spaces.has_key(chars):
                    spaces[chars] = 0

                spaces[chars] += 1
            elif linetype == TAB:
                tabs += 1

    return tabs, spaces, lines

def count_spaces(line):
    count = 0
    line_type = None

    for c in line:
        if c != ' ' and c != "\t":
            return count, line_type

        elif c != line_type and line_type != None:
            return count, line_type

        else:
            count += 1
            if c == ' ':
                line_type = SPACE
            else:
                line_type = TAB

