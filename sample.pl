#!/usr/bin/perl -w
#
#  Sample and print only a certain percentage of input lines.
#

$percent = shift @ARGV;
die $! unless $percent > 0 and $percent < 1;

while(<>) {
    print if rand() < $percent;
}
