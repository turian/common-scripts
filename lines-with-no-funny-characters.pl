#!/usr/bin/perl -w
# Print lines without funny characters
# cf. lines-with-funny-characters.pl
while(<>) {
    print "$_" unless m/([^\s\w\d\/\.\-\{\}\\\:\@\[\]\(\)\+\`\&\'\>\<\$\=\_\#\!\"\!\|\@\#\$\%\^\&\*\~\?\,\.\;])/;
}
