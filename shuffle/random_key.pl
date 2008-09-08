#!/usr/bin/perl
#
# random_key.pl,v 1.1 2004/01/22 04:42:25 turian Exp
#

while(<>) {
	print sprintf("%.32f ", rand()), $_;
}
