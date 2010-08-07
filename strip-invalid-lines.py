#!/usr/bin/python
"""
Strip any line in stdin that cannot be converted from and to utf-8.
"""

from common.str import percent
import sys
print >> sys.stderr, "Reading sys.stdin..."
tot = 0
cnt = 0
for l in sys.stdin:
    tot += 1
    try:
        print l.decode("utf-8").encode("utf-8"),
    except:
        cnt += 1

print >> sys.stderr, "Stripped out %s lines with invalid characters" % percent(cnt, tot)
