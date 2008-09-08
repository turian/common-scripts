#!/usr/bin/python
#
#################################################################
#
#   paired-T-test.py
#
#   USAGE: paired-T-test.py < file
#
#   Given two paired sets X_i and Y_i of n measured values, the paired
#   t-test determines whether they differ from each other in a significant
#   way under the assumptions that the paired differences are independent
#   and identically normally distributed. 
#
#   We assume that each line in STDIN contains two float.
#
#   Confidence intervals:
#   r	90%	95%	97.5%	99.5%
#   1	3.07766	6.31371	12.7062	63.656
#   2	1.88562	2.91999	4.30265	9.92482
#   3	1.63774	2.35336	3.18243	5.84089
#   4	1.53321	2.13185	2.77644	4.60393
#   5	1.47588	2.01505	2.57058	4.03212
#   10	1.37218	1.81246	2.22814	3.16922
#   30	1.31042	1.69726	2.04227	2.74999
#   100	1.29007	1.66023	1.98397	2.62589
#   inf	1.28156	1.64487	1.95999	2.57584
#   from http://mathworld.wolfram.com/Studentst-Distribution.html
#
#
#   $Id: statistics.py,v 1.1 2005/06/24 06:02:24 turian Exp $
#
#
#################################################################

import sys, string
assert(len(sys.argv) == 1)

values = []
for l in sys.stdin:
	(x, y) = string.split(l)
	values.append((float(x), float(y)))

mean = [0.,0.]
n = len(values)
for v in values:
	mean[0] += v[0]
	mean[1] += v[1]
mean[0] /= n
mean[1] /= n

avg = 1.*sum/n

denomsum = 0.
for v in values:
	denomsum += ((v[0] - mean[0]) * (v[1] - mean[1])) ** 2
t = (mean[0] - mean[1]) * sqrt((n * (n - 1)) / denomsum)

print "t = %g" % t
