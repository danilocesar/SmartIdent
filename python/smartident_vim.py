#!/usr/bin/env python

import sys
#import vim
from smartident import utils

filename = sys.argv[1]

handler = utils.SmartFileHandle(filename)
print handler.getRules()
