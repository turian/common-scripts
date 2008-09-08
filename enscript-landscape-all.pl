#!/usr/bin/perl
#
# Enscript all files listed in @ARGV in landscape mode.
# We choose the largest font that won't cause lines to wrap.
#
# enscript-landscape-all.pl,v 1.1 2004/04/11 04:39:08 turian Exp
#

foreach $f (@ARGV) {
	open(F, "< $f") or die $!;
	$width = 0;
	while(<F>) {
		$width = length $_ if length $_ > $width;
	}
	close(F);

	# We can fit 1223 characters with Courier1
	$fontsize = int(1223/$width);
	print "enscript -Plp -r -fCourier$fontsize $f\n";
	system("enscript -Plp -r -fCourier$fontsize $f");
}
