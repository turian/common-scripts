#!/usr/bin/python
#
#  Automatically (heuristically) sort curves in a graph in descending order.
#  Takes into account that curves might not be the same distance.
#  We assume that every x point is at the same fixed interval, e.g. every
#  10K steps, across all curves.
#  [for sake of moving average]
#  We assume each input is two column format, with increasing x value.
#  Potential problem: We use rank violations, not actual distance
#  BUG: We don't count curves with exact same mean. However, this should happen very rarely.
#  BUG: We should randomly tiebreak between curves with same rank error.
#

from common.movingaverage import MovingAverage

import sys, string
assert len(sys.argv) > 1

# Read in all curves
curves = {}
for f in sys.argv[1:]:
    curves[f] = []
#    print f
    for l in open(f):
        x, y = string.split(l)
        curves[f].append((float(x), float(y)))
        if len(curves[f]) > 1:
            # Make sure x values are increasing
            assert curves[f][-1][0] > curves[f][-2][0]

# TODO: Assert fixed internal across all curves

# Find the last x point for each curve, and sort in decreasing order
sortedlastx = []
for f in curves:
    x = curves[f][-1][0]
#    lastx[f] = x
    sortedlastx.append((x, f))
sortedlastx.sort()
sortedlastx.reverse()

sorted_list = []
# Iterate over curves, in order of decreasing last x, and insert into list one at a time.
for (thisx, thisf) in sortedlastx:
    print >> sys.stderr, "Inserting curve with last x = %f, curve = %s" % (thisx, thisf)
    # For all curves in the sorted list and this curve, find the moving average.
    avg = {}
    for f in [thisf] + sorted_list:
        avg[f] = MovingAverage()
        for (x, y) in curves[f]:
            if x > thisx: break
            avg[f].add(y)
#        print >> sys.stderr, "\t", f, avg[f]

    # Figure out which curves are above and below thisf
    above = {}
    below = {}
    for f in sorted_list:
        if avg[f].mean > avg[thisf].mean:
            above[f] = True
        if avg[f].mean < avg[thisf].mean:
            below[f] = True
        # BUG: We don't count curves with exact same mean. However, this should happen very rarely.

#    print >> sys.stderr, "\tAbove %s:" % thisf, above
#    print >> sys.stderr, "\tBelow %s:" % thisf, below

    # For each possible insertion point in sorted_list, compute the number of rank violations
    rankerrors = []
    for i in range(len(sorted_list) + 1):
        err = 0
#        print >> sys.stderr, "\tFor position %d in list" % i
        for f in sorted_list[:i]:
            if f in below:
#                print >> sys.stderr, "\tRank error: Following is below, but list makes it above: %s" % f
                err += 1
        for f in sorted_list[i:]:
            if f in above:
#                print >> sys.stderr, "\tRank error: Following is above, but list makes it below: %s" % f
                err += 1
        rankerrors.append((err, i))
    rankerrors.sort()
    #  BUG: We should randomly tiebreak between curves with same rank error.
#    print >> sys.stderr, "\tSorted list of (rankerrors, position):", rankerrors
    pos = rankerrors[0][1]
    print >> sys.stderr, "Inserting curve at position %d, with %d rank errors: %s" % (pos, rankerrors[0][0], thisf)
    sorted_list = sorted_list[:pos] + [thisf] + sorted_list[pos:]
    sys.stdout.flush()

print string.join(sorted_list, "\n")
