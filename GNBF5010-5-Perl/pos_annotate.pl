use warnings;
use strict;


open snpFile, "pos.txt" or die $!;
my @snp = <snpFile>;
close snpFile;


for my $snp (@snp){
  open annoDB, "hg19_refGene.txt" or die $!;
  chomp($snp);
  my($chr, $pos) = split "\t", $snp;
  #print $chr, "\t", $pos, "\n";
  while(<annoDB>){
    my @fields = split "\t";
    $fields[2] =~ m/chr(\d+)/;
    my $refChr = $1;
    my $strand = $fields[3];
    my $start = $fields[4];
    my $end = $fields[5];
    if ($refChr == $chr){
      if($pos >= $start && $pos <= $end){
        print $chr, "\t", $pos, "\t", $fields[12],"\n";
      }
    }
  }
  close annoDB;
}
