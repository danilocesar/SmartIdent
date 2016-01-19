class MakeFileHandler:
    """
    Makefile handlers uses static rules
    """

    def __init__(self):
        pass

    def getRules(self):
        return ["set autoindent", \
                "set noexpandtab",\
                "set tabstop=4",  \
                "set shiftwidth=4"]
