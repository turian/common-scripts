#!/usr/bin/perl -w
#
# Remove non-ASCII characters

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    s/[^[:ascii:]]+//g;   # get rid of non-ASCII characters
    print;
}
