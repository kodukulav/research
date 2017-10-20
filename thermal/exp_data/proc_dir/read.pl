#!/usr/bin/perl
use Cwd;
$filename = 'new_test.log';

open(my $fh, '<', $filename) or die "Could not open file ";
  
my @comp;
my $count = 0;

while ( $row = <$fh> ) 
{
	chomp $row;
	@store_str = split/,/,$row;
	$comp[$count][0] = $store_str[0];
	$comp[$count][1] = $store_str[1];
	$count++;
}

@all_dir = <*>;

foreach $dir (@all_dir)
{
	if ( -d $dir )
	{
		chdir $dir;
		system ("mkdir move");
		@all_files = <*>;
		for ( $i = 0;$i <= $count; $i++ )
		{
			if ( $dir eq $comp[$i][0] ) 
			{
				system ("mv $comp[$i][1] ./move"); 	
			}
		}	
		
		system ( " rm -f * " );
		system ( " mv ./move/* .; rm -rf move;" );	
		chdir "..";
	}

}
