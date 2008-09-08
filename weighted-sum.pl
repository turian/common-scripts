#!/usr/bin/perl -w
#
#  Given two columns:
#   count   value
#  (e.g. from 'uniq -c')
#  which is SORTED by value,
#  do a weighted sum, and output:
#   sum_of_counts   weighted_sum_of_values
#

$lastval = -999;
$x = 0;
$y = 0;
while(<>) {
    if (m/(\S+)\s+(\S+)/) {
        die $! unless $lastval < $2;
        $x += $1;
        $y += $1 * $2;
        print "$x $y\n";
        $lastval = $2;
    } else {
        die "Could not parse $_";
    }
}
