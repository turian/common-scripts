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
for i, l in enumerate(myopen(f)):
    if i % 1000000 == 0 and i > 0:
        print >> sys.stderr, "\t%d lines read from %s (phase 1 of 2)" % (i, f)
        print >> sys.stderr, stats()
        break
    for w in string.split(l):
        cnt[w] += 1
print >> sys.stderr, "...done reading %s for word freqs" % f
print >> sys.stderr, stats()

print >> sys.stderr, "Delexicalizing %s words with freq<%d..." % (f, minfreq)
print >> sys.stderr, stats()
for i, l in enumerate(myopen(f)):
    break
    if i % 1000000 == 0 and i > 0:
        print >> sys.stderr, "\t%d lines read from %s (phase 1 of 2)" % (i, f)
        print >> sys.stderr, stats()
    for w in string.split(l):
        if cnt[w] < minfreq:
            print UNKNOWN,
        else:
            print w,
    print
print >> sys.stderr, "...done delexicalizing %s words with freq<%d" % (f, minfreq)

keep = 1    # Start at 1, not zero, for *UNKNOWN*
for w in cnt:
    if cnt[w] >= minfreq: keep += 1
from common.str import percent
print >> sys.stderr, "Vocabulary is now %s words" % percent(keep, len(cnt))
print >> sys.stderr, stats()
