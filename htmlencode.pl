#!/usr/bin/perl -w
#
# Encode HTML entities, e.g. < becomes &lt;

use HTML::Entities;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    print encode_entities($_);   # Encode HTML entities
}
