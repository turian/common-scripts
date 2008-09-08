#!/usr/bin/perl -w
#
# Code does not work.
# from: http://www.eyrie.org/~eagle/notes/cvs/revisions.html
# Russ Albery writes:
# If you do want to use the CVS revision number as the version number
# of a Perl script, I use the following code or something similar using
# Getopt::Long to handle the -v or --version command-line option

using GetOpt::Long;

$ID = q$\Id$;  # Remove the \ so that Id will be expanded.

# [...]
if ($ARGV[0] =~ /^-.*v) {
	my $version = join (' ', (split (' ', $ID))[1..3]);
	$version =~ s/,v\b//;
	$version =~ s/(\S+)$/($1)/;

	# I change from die to print -jpt
#	die $version, "\n";
	print $version, "\n";
}
