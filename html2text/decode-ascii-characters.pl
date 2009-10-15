#!/usr/bin/perl -w
#
# Decode HTML entities, e.g. &lt; becomes <, unless it becomes a non-ASCII character.


use HTML::Entities;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    # Decode all entities, then re-encode non-ascii characters.
    $s = decode_entities($_);
    $s =~ s/([^[:ascii:]]+)/encode_entities($1)/eg;   # get rid of non-ASCII characters
    print $s;
}
