#!/usr/bin/perl

use warnings;
use strict;

# scalar: numbers
my $a = 1;
my $b = 1.2;

print $a + $b, "\n";

# scalar: strings
print "香港，你好！\n";
print "Hello, Hongkong!\n";
print "中國，你好！\n";

print "Hello "x10;
print "\n";

my $fname = "Chen";
my $gname = "Gang";
my $name = $gname." ".$fname;
print "$name\n";
$name = $gname, " ", $fname;
print "$name\n";
print $gname, " ", $fname, "\n";

# conversion between numbers and strings
print 1 + 2, "\n";
print "1" + 2, "\n";
print "1" + "2", "\n";
print "1 + 2", "\n";

print "00001" + "002", "\n";

print "one" + 2, "\n";
print "one" + "two", "\n";

# if control structure
my $num1 = 5;
my $num2 = 3;

if($num1 > $num2){
  print "Success\n";
}else{
  print "failed\n";
}

$num1 > $num2 ? print "Success\n" : print "Failed\n";

print "Success\n" if ($num1 > $num2);

# while and for
my $num = 1;
while($num < 10){
  print $num, "\n";
  $num++;
}

for($num = 1;$num<10;$num++){
  print $num, "\n";
}

# list and array
my @list1 = (1,2,3,4,5);
my @list2 = ("one", "two", "three");
my @list3 = (1..10);
print $list1[0], "\n";
print $list2[1], "\n";
print $list3[3], "\n";

# foreach
foreach (@list1){
  print $_, "\n";
}

for(@list1){
  print $_, "\n";
}

print $_, "\n" for(@list1);

print $_, "\n" for(1..10);
