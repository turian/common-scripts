#!/usr/bin/perl -w
#
#################################################################
#
#  rzip.pl
#
#  USAGE: rzip.pl file1 [file2 ...]
#
#  Call rzip on each file in @ARGV.
#  Since rzip is disk I/O limited, we copy the file to /tmp before
#  attempting to rzip it.
#
#  $Id: rzip.pl,v 1.4 2004/12/15 13:44:12 turian Exp $
#
#
#################################################################

die "Incorrect call.\nUSAGE: rzip.pl file1 [file2 ...]\n" unless scalar @ARGV > 0;

$rzip = "/home/turian/utils/bin/rzip";

use File::Temp qw/ tempfile tempdir /;

foreach $f (@ARGV) {
#	(my $fh, my $tmpf) = tempfile( DIR => "/tmp" );
	(my $fh, my $tmpf) = tempfile( DIR => "/data/turian/temp" );

#	print STDERR ("nice -10 cp $f $tmpf && $rzip -P $tmpf && mv $tmpf.rz $f.rz && rm -f $tmpf $tmpf.rz $f\n");
	system("nice -10 cp $f $tmpf && nice -10 $rzip -P $tmpf && mv $tmpf.rz $f.rz && rm -f $tmpf $tmpf.rz $f\n");
}
