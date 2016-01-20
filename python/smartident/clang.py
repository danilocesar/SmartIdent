import os

class ClangFormatLocator:
    """
    This class will take care of reading recursively folders
    and try to find the clang-format file
    """

    # This should be read in the future using a vim option,
    # but lets assume it's 5 for now
    RECURSION = 5

    def __init__(self, dirname):
        self.__dirname = dirname
        self.__rules = []

    def searchAndReadClangFormatFile(self):
        """
        This method should read recursivelly the current dirname
        looks for .clang-format files.

        In case one if found, it should read and return True,
        otherwise return False.
        """
        startPath = self.__dirname
        for _ in range(self.RECURSION):
            filename = os.path.join(startPath, ".clang-format")
            if (os.path.isfile(filename)):
                self.__processClangFile(filename)
                return True

            startPath = os.path.abspath(os.path.join(startPath, "../"))

        return False

    def getRules(self):
        return self.__rules

    def __processClangFile(self, filename):
        """
        This method process a clang-format file looking for
        specific pairs of elements
        """
        lines = [line.rstrip('\n') for line in open(filename)]

        # Perhaps we should read all entries before trying to process them...
        # something to think about after the first release

        for rule in lines:
            key, val = rule.split(":", 1)

            if key.strip() == "UseTab":
                if val in ["Always", "ForIndentation"]:
                    self.__rules.extend(["set autoindent", \
                                         "set noexpandtab"])
                else:
                    self.__rules.append("set expandtab")

            if key.strip() == "TabWidth":
                self.__rules.extend(["set autoindent",
                                     "set tabstop=" + val])

            if key.strip() == "IndentWidth":
                self.__rules.extend(["set autoindent",
                                     "set shiftwidth=" + val])
