#!/usr/bin/python
#
#################################################################
#
#   choose-columns.py
#
#   USAGE: choose-columns.py col1,... < file
#
#   Given a comma-separated list of columns as command-line arguments,
#   select those columns and output them from each line in stdin.
#
#   choose-columns.py,v 1.1 2006/04/07 23:58:49 turian Exp
#
#
#################################################################


import sys, string
assert len(sys.argv) == 2
cols = [int(i)-1 for i in string.split(sys.argv[1], ",")]
for l in sys.stdin:
	l = string.split(l)
	for c in cols:
		print l[c],
	print
