#!/usr/bin/perl -w
#
# Remove non-UTF 1.1 characters
# From http://stackoverflow.com/questions/1016910/how-can-i-strip-invalid-xml-characters-from-strings-in-perl/1477316#1477316

#binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
while(<>) {
    # allowed: [#x1-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]
    s/[^\x01-\x{D7FF}\x{E000}-\x{FFFD}\x{10000}-\x{10FFFF}]//go;
    # restricted:[#x1-#x8][#xB-#xC][#xE-#x1F][#x7F-#x84][#x86-#x9F]
    s/[\x01-\x08\x0B-\x0C\x0E-\x1F\x7F-\x84\x86-\x9F]//go;
    print;
}
