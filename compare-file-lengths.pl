#!/usr/bin/perl -w
#
########################################################################
#
#
#   compare-file-lengths.pl
#
#   USAGE: ./compare-file-lengths.pl file1 file2 [...]
#
#   Make sure that all files given on command-line have the same number
#   of lines.
#
#   $Id: compare-file-lengths.pl 715 2004-09-27 22:16:22Z turian $
#
#
#######################################################################

die unless scalar @ARGV >= 2;

$lengths = {};
foreach (@ARGV) {
	$lengths{$_} = int(`wc -l < $_`);
}

$to_die = 0;
foreach $f1 (keys %lengths) {
	foreach $f2 (keys %lengths) {
		next if $f1 ge $f2;
		if ($lengths{$f1} != $lengths{$f2}) {
			$to_die = 1;
			print STDERR "Number of lines mismatch: $f1 ($lengths{$f1}) vs. $f2 ($lengths{$f2})\n";
		}
	}
}

die if $to_die;
