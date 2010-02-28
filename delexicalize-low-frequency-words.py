#!/usr/bin/python
#
#################################################################
#
#   delexicalize-low-frequency-words.py
#
#   USAGE: ./delexicalize-low-frequency-words.py minfreq file
#
#   Delexicalize all words with freq less than minfreq to *UNKNOWN*
#
#################################################################

UNKNOWN = "*UNKNOWN*"

import sys, string
assert len(sys.argv) == 3
minfreq = int(sys.argv[1])
f = sys.argv[2]

from common.file import myopen
from common.stats import stats

from collections import defaultdict
cnt = defaultdict(int)

print >> sys.stderr, "Reading %s for word freqs..." % f
print >> sys.stderr, stats()
for l in myopen(f):
    for w in string.split(l):
        cnt[w] += 1
print >> sys.stderr, "...done reading %s for word freqs" % f
print >> sys.stderr, stats()

print >> sys.stderr, "Delexicalizing %s words with freq<%d..." % (f, minfreq)
print >> sys.stderr, stats()
for l in myopen(f):
    for w in string.split(l):
        if cnt[w] < minfreq:
            print UNKNOWN,
        else:
            print w,
    print
print >> sys.stderr, "...done delexicalizing %s words with freq<%d" % (f, minfreq)
print >> sys.stderr, stats()
