#!/usr/bin/python
#
#################################################################
#
#   cumulative.py
#
#   USAGE: cumulative.py < file
#
#   Output a cumulative sum for each line in the input file.
#
#   We assume that for each line in STDIN, the first column is a float
#   and the rest of the string is a description.
#   (Output from 'uniq -c' works nicely.)
#
#   TODO:
#    * Determine if values are ints or floats.
#    * Prettier output.
#
#   cumulative.py,v 1.1 2005/06/24 06:46:43 turian Exp
#
#
#################################################################

import re, sys
assert(len(sys.argv) == 1)

numre = re.compile("^\s*([0-9\.e\-\+]+)\s+(.*\S)\s*$")

values = []
tot = 0
for l in sys.stdin:
    m = numre.match(l)
    assert m
    (a, b) = (float(m.group(1)), m.group(2))
    tot += a
    print tot, b
