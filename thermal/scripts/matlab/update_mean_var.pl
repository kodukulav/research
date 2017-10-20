#!/usr/bin/perl
use strict;
use warnings;

## Argument 0 is file name
## Argument 1 is led_array
## Argument 2 is hot_temp 
## Argument 3 is with_hot_pixel

my $filename = $ARGV[0];
my $new_file = $filename."modified";

open my $ifh, '<' , $filename or die "couldn't open the file $filename";
open my $ofh, '>' , $new_file or die "couldn't open the file $new_file";

while ( <$ifh> )
{
	if ( $_ =~ /led_array\s+=\s+/ )
	{
		my $line = "led_array = [".$ARGV[1]."];"."\n";
		print $ofh $line;
	}
	elsif ( $_ =~ /int2str\(hot_temp_arr\(/ )
	{
		my $line = "hot_temp = int2str(hot_temp_arr(".$ARGV[2]."));"."\n";
		print $ofh $line;
	}
	elsif ( $_ =~ /with_hot_pixel\s+=\s+/ )
	{
		my $line = "with_hot_pixel = ".$ARGV[3].";\n";
		print $ofh $line;
	}
	else
	{
		print $ofh $_;	
	}
}

close $ifh;
close $ofh;	

# In the case of subplot matlab files 
# directory name is also specified in unix format
# changing it to windows format for the move command to work below
$new_file =~ s/\//\\/g;
$filename =~ s/\//\\/g;


system ( "move $new_file $filename" );
