import sys

filename = sys.argv[1]

SPACE = 1
TAB = 2

def count_spaces(line):
    count = 0
    line_type = None

    for c in line:
        if c != ' ' and c != "\t":
            return count, line_type

        else:
            count += 1
            if c == ' ':
                line_type = SPACE
            else:
                line_type = TAB

spaces = {}
tabs = 0
with open(filename, 'rb', 1024*1024) as f:
    for line in f:
        # break in case we don't find line starting with space or tab
        if not (line.startswith(' ') or line.startswith('\t')):
            continue

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

print tabs, spaces.values()
