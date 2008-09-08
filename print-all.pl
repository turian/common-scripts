#!/usr/bin/perl -w
#
# For each file (.ps or .pdf) specified as a command-line argument,
# print the file to a random printer.
# Files over 100 pages are printed two-pages-per-sheet
#
# $Id: print-all.pl,v 1.1 2004/01/22 04:42:23 turian Exp $
#

$maxpages = 100;	# Files over 100 pages are printed two-pages-per-sheet
$toomanypages = 200;	# Files over 200 pages are not printed
#@printers = ("lp", "nhp2");
#@printers = ("nhp2");
@printers = ("lp");

srand();

sub pagecount {
	(my $fil) = @_;
	$txt = `a2ps -1 -o /dev/null $fil 2>&1`;
	if ($txt =~ m|([0-9]+) pages|) {
		return $1;
	} else {
		return 0;
	}
}

foreach $fil (@ARGV) {
	next if not $fil =~ /\S/;
#	print STDERR "Pagecounting $fil\n";
	my $p = pagecount($fil);
	my $lp = $printers[int(rand() * (scalar @printers))];
#	print STDERR "Printing to $lp\n";
	if ($p > $maxpages) {
		if ($p > $toomanypages) {
			print STDERR "$fil has too many pages ($p pages)\n";
		} else {
			print "a2ps -P$lp -q -2 $fil\n";
			system("a2ps -P$lp -q -2 $fil");
		}
	}
	if ($fil =~ /\.pdf$/i or $fil =~ /\.ps.gz$/i) {
#		print STDERR "$fil is a PDF\n";
		if ($p <= 0) {
			# Must use acroread because of weird PDF
			print STDERR "Print $fil with acroread\n";
		} else {
			print "a2ps -q -1 -P$lp $fil\n";
			system("a2ps -q -1 -P$lp $fil");
		}
	} elsif ($fil =~ /\.ps$/i) {
#		print STDERR "$fil is PostScript\n";
		if ($p <= 0) {
			print STDERR "Cannot handle $fil\n";
		} else {
			print "lpr -P$lp $fil\n";
			system("lpr -P$lp $fil");
		}
	} else {
		print STDERR "$fil is of unknown type\n";
	}
}
