#!/usr/bin/perl
#
# Given input lines which are formatted in columns, output on a single
# line the Nth column value from all lines of input.
# (Strips leading and trailing whitespace before determining columns.)
#

die unless scalar @ARGV == 1;
$N = $ARGV[0]-1;
die unless $N >= 0;

$str = "";
while(<STDIN>) {
	s/^\s+//;
	s/\s+$//;
	@words = split(/\s+/, $_);
#	die unless scalar @words > $N;
	print STDERR "Could not chop: $_" unless scalar @words > $N;
	$str .= " $words[$N]";
}
$str =~ s/^\s+//;
print "$str\n";
