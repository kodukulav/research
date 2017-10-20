use Cwd;

$config  = $ARGV[0]; print $config."\n";
$LED_set = $ARGV[1]; print $LED_set."\n";
$img_num = $ARGV[2]; print $img_num."\n";
$run_dir = $ARGV[3]; print $run_dir."\n";


$img_num = $img_num.".jpg"; print $img_num."\n";

if ( $run_dir ne "" ) {
	$concat_dir = $config."_".$LED_set."_".$run_dir."_"; 
	#print $concat_dir."\n"; 
}


else { 
	#print "Empty String".$run_dir."\n";
	$concat_dir = $config."_".$LED_set."_"; }
	


@all_dir = <*>;


foreach $dir (@all_dir)
{
	# print $dir."\n";
	if ( ($dir =~ m/${concat_dir}.*/) && ( $dir =~ m/.*_r10_.*/ ) )
	{
		print $dir."\n";
		system("cd $dir;start $img_num;cd ..;");
		sleep(10);
		# print $dir."\n";
	}
	
} 
