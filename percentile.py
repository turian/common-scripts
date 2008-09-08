#!/usr/bin/python
#
#################################################################
#
#   percentile.py
#
#   USAGE: percentile.py < file
#
#   Output a percentile for each line in the input file (sorted).
#
#   We assume that for each line in STDIN, the first column is a float
#   and the rest of the string is a description.
#   (Output from 'uniq -c' works nicely.)
#
#   TODO:
#	* Determine if values are ints or floats.
#	* Prettier output.
#
#   percentile.py,v 1.1 2005/06/24 06:46:43 turian Exp
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
	values.append((a, b))
#values.append((tot, "TOTAL"))
values.sort()
values.reverse()

for (a, b) in values:
	print "%.2f%%\t%s\t\t(%.2f/%.2f)" % (100.*a/tot, b, a, tot)
