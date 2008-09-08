#!/usr/bin/perl -w
#
# Issue command '$ARGV[0]' (*with* single-quotes added) on all cluster machines.
#

die $! unless scalar @ARGV == 1;
$cmd = $ARGV[0];
#$cmd =~ s|'|\\\\'|g;

@machines = ("c1.cs.nyu.edu", "c10.cs.nyu.edu", "c11.cs.nyu.edu", "c12.cs.nyu.edu", "c13.cs.nyu.edu", "c14.cs.nyu.edu", "c15.cs.nyu.edu", "c16.cs.nyu.edu", "c17.cs.nyu.edu", "c2.cs.nyu.edu", "c3.cs.nyu.edu", "c4.cs.nyu.edu", "c5.cs.nyu.edu", "c6.cs.nyu.edu", "c7.cs.nyu.edu", "c8.cs.nyu.edu", "c9.cs.nyu.edu", "crunchy2.cims.nyu.edu", "csstupc53.cs.nyu.edu", "m1.cs.nyu.edu", "s1.cs.nyu.edu", "int1.cims.nyu.edu", "int4.cims.nyu.edu", "int4.cims.nyu.edu", "int4.cims.nyu.edu");
#@machines = ("box11.cims.nyu.edu", "c1.cs.nyu.edu", "c10.cs.nyu.edu", "c11.cs.nyu.edu", "c12.cs.nyu.edu", "c13.cs.nyu.edu", "c14.cs.nyu.edu", "c15.cs.nyu.edu", "c16.cs.nyu.edu", "c17.cs.nyu.edu", "c2.cs.nyu.edu", "c3.cs.nyu.edu", "c4.cs.nyu.edu", "c5.cs.nyu.edu", "c6.cs.nyu.edu", "c7.cs.nyu.edu", "c8.cs.nyu.edu", "c9.cs.nyu.edu", "crunchy2.cims.nyu.edu", "csstupc53.cs.nyu.edu", "euler08.cims.nyu.edu", "m1.cs.nyu.edu", "s1.cs.nyu.edu");

foreach $m (@machines) {
	$x = "ssh $m '$cmd'";
	print "$x\n";
	system($x);
}
