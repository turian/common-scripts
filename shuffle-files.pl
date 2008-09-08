#!/usr/bin/perl -w

use List::Util 'shuffle';

@fs = split(/[\r\n]+/, `find . -type f`);
@fnew = ();
$i = 0;
foreach $f (@fs) {
    print STDERR "WARNING: $f" if $f =~ m/"/;
#    push(@fnew, "\"$f\"");
    push(@fnew, "$f");
    $i++;
#    last if $i >= 10;
}
@fnew = shuffle(@fnew);
print join("\n", @fnew);
print STDERR join("\n", @fnew);
