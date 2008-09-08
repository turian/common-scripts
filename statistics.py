#!/usr/bin/python
#
#################################################################
#
#   statistics.py
#
#   USAGE: statistics.py < file
#
#   Sort + compute statistics:
#   Mean, median, and standard deviation
#
#   We assume that each line in STDIN contains single float.
#
#   TODO:
#	* Double-check confidence interval computation!
#
#   $Id: statistics.py,v 1.1 2005/06/24 06:02:24 turian Exp $
#
#
#################################################################

import sys
assert(len(sys.argv) == 1)

values = []
for l in sys.stdin:
	values.append(float(l))
values.sort()

sum = 0
n = len(values)
for x in values:
	sum += x

avg = 1.*sum/n

var = 0
for x in values:
	var += (x - avg) * (x - avg)

if len(values) % 2 == 1:
	median = values[len(values)/2]
else:
	median = (values[len(values)/2-1] + values[len(values)/2])/2.

print "Count:\t%d" % len(values)
print "Mean:\t%.6g" % avg
print "Median:\t%.6g" % median
print "Stddev:\t%.6g" % (1.*var/n)**.5
print "Stddev:\t%.6g (bias-corrected)" % (1.*var/(n-1))**.5
#print "95%% CI:\t%.6g (+-) [NB this value may be fucked!]" % ((1.*var)**.5/n * 1.95996)
#print "95%% CI:\t%.6g (+-) [NB this value may be fucked!]" % ((1.*var)**.5/n * 1.95996)
print "95%% CI:\t%.6g (+-) [NB this value may be fucked!]" % ((1.*var/n)**.5 * 1.95996)
print "95%% CI:\t%.6g (+-) [NB this value may be fucked!]" % ((1.*var/n)**.5 * 1.95996)

import sys
sys.path.append('/home/turian/utils/lib/python2.3/site-packages')

import goopy.functional
print "Goog mean:\t%.6g" % goopy.functional.mean(values)
print "Goog stddev:\t%.6g" % goopy.functional.stddev(values)
print "max:\t%.6g" % goopy.functional.maximum(cmp, values)
print "min:\t%.6g" % goopy.functional.minimum(cmp, values)
