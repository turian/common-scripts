#!/usr/bin/perl
#
# Fetch PDFs from citeseer. STDIN should be a list of URLs.
#
# $Id: citeseer-get.pl,v 1.1 2004/01/22 04:42:23 turian Exp $
#

$sleepmin = 5;		# Minimum amount of time to sleep between fetchs
$sleepmax = 15;		# Maximum amount of time to sleep between fetchs

srand();

sub fetchsleep {
	$sleeptime = int(rand() * ($sleepmax - $sleepmin) + $sleepmin);
#	print "Sleeping for $sleeptime secs...\n";
	sleep $sleeptime;
}

$first = 1;
while (<>) {
	next if not /\S/;
	chop;
	$url = $_;
	if (not $url =~ m|http://citeseer.nj.nec.com/|) {
		print STDERR "$url is not at Citeseer. Skipping...\n";
		next;
	}
	if ($first) {
		$first = 0;
	} else {
		fetchsleep();
	}
	print "Fetching $url...\n";
	$txt = `wget -O - -U lynx -q $url`;
	if ($txt =~ m|<a href="([^"]*)"[^>]*>PDF</a>|i) {
		$pdfurl = $1;
		$pdfurl =~ s|.*(http://citeseer.nj.nec.com/)|$1|;
		fetchsleep();
		($pdffil = $pdfurl) =~ s|.*/||;
		if (-e $pdffil) {
			print STDERR "$pdffil already exists. Skipping...\n";
			next;
		}
		print "Getting $pdffil...\n";
		system("wget -U lynx -q '$pdfurl'");
#		system("wget -U lynx -q '$pdfurl'")
#			or print STDERR "Error in wget of $pdfurl.\n";
	} else {
		print STDERR "Could not grep PDF in $url. Skipping...\n";
#		print "$txt\n";
		next;
	}
}
