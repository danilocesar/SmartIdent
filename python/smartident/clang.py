class ClangFormatLocator:
    """
    This class will take care of reading recursively folders
    and try to find the clang-format file
    """

    # This should be read in the future using a vim option,
    # but lets assume it's 3 for now
    RECURSION = 5

    def __init__(self, dirname):
        self.__dirname = dirname

    def searchAndReadClangFormatFile(self):
        """
        This method should read recursivelly the current dirname
        looks for .clang-format files.

        In case one if found, it should read and return True,
        otherwise return False.
        """

        # TODO: Implement
        # if find clang-format, then call processClangFile
        return None

    def __processClangFile(self):
        """
        This method process a clang-format file looking for
        specific pairs of elements
        """

        # TODO: Implement
        pass
