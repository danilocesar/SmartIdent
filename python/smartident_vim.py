#!/usr/bin/env python

import sys
import vim
import utils

filename = sys.argv[1]

SPACE = 1
TAB = 2


print utils.processFile(filename)
