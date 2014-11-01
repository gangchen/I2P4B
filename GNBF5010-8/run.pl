use warnings;
use strict;

my $a = 1.3;
my $b = 0.7;
my $c = 0.6;

my $strA = "Hello";
my $strB = "Perl";


print $a-$b, "\n";

print $strA." ".$strB, "\n";

if($a - $b == $c){
  print "1.3 - 0.7 is equal to 0.6\n";
}else{
  print "1.3 - 0.7 is not equal to 0.6\n";
}
