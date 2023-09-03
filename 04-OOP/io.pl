#!/usr/bin/perl

use warnings;
use strict;


# input from user
# print "What's your name?\n";
#
# my $name = <STDIN>;
# print "Hello ", $name;
#
# my @names = <STDIN>;
#
# print "Hello ", $_ for(@names);

# interact with file
open inFile, "names.txt" or die $!;
open outFile, ">scores.txt" or die $!;
open addFile, ">>scores.txt" or die $!;
while(<inFile>){
  print $_;
}
close inFile;

for(1..10){
  print outFile $_,"\n";
}
close outFile;

for(11..20){
  print addFile $_, "\n";
}
close addFile;
