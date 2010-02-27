#!/usr/bin/perl
#
# clean.pl,v 1.1 2004/01/22 04:42:25 turian Exp
#

while(<>) {
	if (/[0-9\.]+\s(.*)/s) {
		print $1;
	} else {
		die "Cannot parse: $_";
	}
}
