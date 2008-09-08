#!/usr/bin/perl -w

open(SORT, "| sort | uniq -c | sort -rn");
$cnt = 0;
$txt = "";
while(<>) {
	print SORT "$1\n" if /undefined reference to (.+)/;
	$cnt++ if /undefined reference to (.+)/;
	$txt .= $_;
}
close SORT;

print $txt if $cnt == 0;
