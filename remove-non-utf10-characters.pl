#!/usr/bin/perl -w
#
# Remove non-UTF 1.0 characters
# From http://stackoverflow.com/questions/1016910/how-can-i-strip-invalid-xml-characters-from-strings-in-perl/1477316#1477316

#binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    # #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]
    s/[^\x09\x0A\x0D\x20-\x{D7FF}\x{E000}-\x{FFFD}\x{10000}-\x{10FFFF}]//go;
    print;
}
