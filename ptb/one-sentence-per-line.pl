#!/usr/bin/perl -w
#
#  Output one sentence per line, using PTB tagged/ files.
#       ./one-sentence-per-line.pl ~/data/PennTreebank2/tagged/wsj/*/*pos
#

foreach $f (@ARGV) {
    print STDERR "$f\n";
    open(F, "<$f") or die $!;
    while(<F>){
        chop;
        next if /^=============/;
        print "\n" if $_ eq "";
        s/[\[\]]//g;
        s/^\s+//g;
        s/\/\S+//g;
        print;
    }
}
