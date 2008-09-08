#!/usr/bin/perl -w
#
# Convert a PostScript file to one that forces single-sided printing.
#

$found = 0;
while(<>) {
	if (not $found and not /^\S*\%/) {
		print "statusdict /setduplexmode known
			{ statusdict begin false setduplexmode end } if\n";
		$found = 1;
	}
	print;
}
