@all_dir = <*>;


foreach $dir (@all_dir)
{
	if ($dir =~ m/^32ms_1x_40_.*$/ )
	{
		@cut_string = split /_/,$dir;
		$time = $cut_string[-1];
		$new_time = substr($time,0,2)."_".substr($time,2,2);
		print $new_time.",";		
	}	

}
