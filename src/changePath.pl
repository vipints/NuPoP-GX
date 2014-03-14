#!/usr/local/bin/perl
#use strict;
use Cwd;

#system('cp Npred.f90.back Npred.f90');
my $cwd=getcwd();
open (OLD,"Npred.f90");
my @lines=<OLD>;
close(OLD);
open (NEW,">Npred.f90");
my $i=0;
my $current;
for ($i==0;$i<=$#lines;$i++){
  if($lines[$i]=~m/freqL.txt/){
    $current="  open(1,file='".$cwd."/profile/freqL.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/tranL.txt/){
    $current="  open(1,file='".$cwd."/profile/tranL.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/tranL2.txt/){
    $current="  open(1,file='".$cwd."/profile/tranL2.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/tranL3.txt/){
    $current="  open(1,file='".$cwd."/profile/tranL3.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/tranL4.txt/){
    $current="  open(1,file='".$cwd."/profile/tranL4.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/147freqN.txt/){
    $current="  open(1,file='".$cwd."/profile/147freqN.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/147tranN.txt/){
    $current="  open(1,file='".$cwd."/profile/147tranN.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/146-149freqN4.txt/){
    $current="  open(1,file='".$cwd."/profile/146-149freqN4.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/146-149tranN4.txt/){
     $current="  open(1,file='".$cwd."/profile/146-149tranN4.txt')";
     $lines[$i] =$current;
     print NEW $lines[$i],"\n";
  }
   elsif ($lines[$i]=~m/Pd.txt/){
    $current="  open(1,file='".$cwd."/profile/Pd.txt')";
    $lines[$i] =$current;
    print NEW $lines[$i],"\n";
  }
  else{print NEW $lines[$i]};
}
close NEW;
