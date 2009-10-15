#!/usr/bin/perl -w
#
# Decode HTML entities, e.g. &lt; becomes <

use HTML::Entities;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    print decode_entities($_);   # Decome HTML entities
}
