#!/usr/bin/perl -w

#$count = 4000;
$count = 2000;
#$count = 1000;
#$count = 500;
$min_images_per_directory = 5;
$max_images_per_directory = -1;
#$min_images_per_directory = 0;
#$max_images_per_directory = 20;

$count = $ARGV[0] if scalar @ARGV == 1;

use List::Util 'shuffle';

@gals = split(/[\r\n]+/, `find . -type d -follow`);
@gals = shuffle(@gals);
$lst = "";
foreach $g (@gals) {
	next if -e "$g/BLOCKED";	# Skip blocked galleries
    $gnew = $g;
    $gnew =~ s/"/\\"/g;
#	$cmd = "ls \"$gnew/\"*jpg 2> /dev/null";
	$cmd = "ls \"$gnew/\"*jpg";

	$files = `$cmd`;
    $files =~ s/ /\\ /g;
	@thisf = split(/\S+/, $files);
	next if scalar @thisf < $min_images_per_directory;
	next if (scalar @thisf > $max_images_per_directory && $max_images_per_directory > 0);

	$lst = $lst . $files;

	@allf = split(/\S+/, $lst);
	last if scalar @allf > $count;
}

open(O, "| xargs xv");
#print $lst;
print O $lst;
