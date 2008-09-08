#!/usr/bin/perl -w
#
# For each file (usually .ps or .pdf) specified in stdin,
# count the number of pages in the file
#
# page-count.pl,v 1.1 2004/01/22 04:42:23 turian Exp
#

sub pagecount {
	(my $fil) = @_;
	$txt = `a2ps -1 -o /dev/null $fil 2>&1`;
	if ($txt =~ m|([0-9]+) pages|) {
		print "$1 pages in $fil \n";
	} else {
		print STDERR "Could not find page count of $fil. Skipping...\n";
	}
}

foreach $fil (@ARGV) {
	pagecount($fil)
}

exit if scalar (@ARGV) == -1;

while (<STDIN>) {
	next if not /\S/;
	chop;
	$fil = $_;
	pagecount($fil);
}
