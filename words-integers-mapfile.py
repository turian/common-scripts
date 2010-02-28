#!/usr/bin/python
#
#  USAGE:
#   ./words-integers-mapfile.py < textfile
#
#  Create a integers mapfile for the words in textfile.
#  mapfile contains lines of the form
#       word
#  The line number in mapfile (starting at 0) is the ID of a word.
#  *UNKNOWN* is a special word which will be added if it is not in the
#  mapfile, and will always have ID 0. If *UNKNOWN* is added to the
#  mapping, the line numbering will start at 1 not 0.
#

import sys, string
from common.file import myopen
from common.mydict import sort as dictsort

from collections import defaultdict
cnt = defaultdict(int)
for l in sys.stdin:
    for w in string.split(l):
        if w != "*UNKNOWN*":
            cnt[w] += 1

assert "*UNKNOWN*" not in cnt
words = ["*UNKNOWN*"] + [t[1] for t in dictsort(cnt)]
for w in words:
    print w
