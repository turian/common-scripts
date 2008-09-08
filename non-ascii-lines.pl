#!/usr/bin/perl -w
#
#  Print the line numbers that contain non-ascii, for each file in @ARGV
#
# non-ascii-lines.pl,v 1.2 2007/03/21 23:05:45 turian Exp

foreach $f (@ARGV) {
	open(F, "$f") or next $!;
	$l = 0;
	while(<F>) {
		$l++;
		if (/([^A-Za-z0-9\=\+\-\.\s\#\:_\(\)\[\]\'\"\$\,\%\&\;\>\@\\\/\*\<\!\?])/) {
			print "$f:$l '$1' $_";
		}
	}
	close F;
}
