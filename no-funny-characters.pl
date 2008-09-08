#!/usr/bin/perl -w
# Print lines without funny characters
# cf. funny-characters.pl
while(<>) {
    print "$_" unless m/([^\s\w\d\/\.\-\{\}\\\:\@\[\]\(\)\+\`\&\'\>\<\$\=\_\#\!\"\!\|\@\#\$\%\^\&\*\~\?\,\.\;])/;
}
