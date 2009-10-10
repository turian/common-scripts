#!/usr/bin/python
#
#  USAGE:
#   ./words-to-integers.py mapfile textfile
#
#  Each word in textfile will be converted to a number, according to the mapping in mapfile.
#
#  mapfile contains lines of the form
#       word stuff
#  The line number in mapfile (starting at 0) is the ID of a word.
#  *UNKNOWN* is a special word which will be added if it is not in the
#  mapfile, and will always have ID 0. If *UNKNOWN* is added to the
#  mapping, the line numbering will start at 1 not 0.
#

import sys, string
from common.file import myopen

assert len(sys.argv) == 3
map = {}
cnt = 0
for l in myopen(sys.argv[1]):
    lst = string.split(l)
    w = lst[0]
    if w == "*UNKNOWN*": assert cnt == 0
    if cnt == 0:
        if w != "*UNKNOWN*":
            map["*UNKNOWN*"] = cnt
            cnt += 1
    map[w] = cnt
    cnt += 1
assert map["*UNKNOWN*"] == 0

for l in myopen(sys.argv[2]):
    for w in string.split(l):
        if w in map: print map[w],
        else: print map["*UNKNOWN*"],
    print
