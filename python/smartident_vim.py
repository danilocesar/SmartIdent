#!/usr/bin/env python

import sys
import vim
import utils

filename = sys.argv[1]

SPACE = 1
TAB = 2


tabs, spaces, lines = utils.processFile(filename)
print lines, tabs

# define that tab-indent files should have more than 50% of lines
# starting with tabs
if (tabs / float(lines) > 0.5):
    print "USE TABS"
