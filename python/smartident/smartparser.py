class SmartParser:
    """ SmartParser

    This class tries to extract from the file the rules used to build it 
    """

    def __init__(self, url):
        self.__url = url
        self.__rules = []

        self.__processFile(url)

    def getRules(self):
        return self.__rules

    def __processFile(self, filename):
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

                # ignore possible comments
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

                chars, linetype = self.count_spaces(line)
                if linetype == SPACE:
                    if not spaces.has_key(chars):
                        spaces[chars] = 0

                    spaces[chars] += 1
                elif linetype == TAB:
                    tabs += 1

        return tabs, spaces, lines

    def count_spaces(self, line):
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

