#!/usr/bin/perl -w
#
# Encode all non-ascii text as HTML entities.

use HTML::Entities;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    s/([^[:ascii:]]+)/encode_entities($1)/eg;   # get rid of non-ASCII characters
    print;
}
