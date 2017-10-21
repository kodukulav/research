To generate the noise models from the raw image data 
collected from the image sensor matlab scripts are used

Directory Structure:
exp_data  --------> Raw Image Data
proc_data --------> Results after processing the Raw Image Data
scripts/matlab ---> Matlab scripts  
scripts/python ---> Python scripts to measure task accuracy
task_accuracy ----> Raw Image data used to measure task accuracy

Matlab Scripts: 
To build the noise models using matlab please follow the instructions below:
1. Open matlab software ( we have used MATLAB R2017a for our runs)
2. Open mean_var_changed.m script and modify the following variables to run as per your needs 
	a. Set git_proc_data_path and git_exp_data_path to point to proc_data and exp_data folders in the top thermal folder 
	b. Set hot_temp to one of the values in hot_temp_arr
	c. Set led_array to 1/2/3/4 or a combination of these to capture results at LED setting 0/3/5/6 respectively
  	d. Set with_hot_pixel to generate results with or without hot pixels 
3. Then run the script using Fn+F5. Observe the plots generated in the proc_data directory for the runs finished  

mean_var_changed.m --->  calculate mean,standard deviation for 32ms_4X configuration of the image sensor 
						 across temperatures( 48,56,68,80,92C ) and LED settings( 0,3,5,6 )  


hot_pixels_calc.m ---->  Measure hot pixels for 32ms_4X configuration of the image sensor 
						 across temperatures( 48,56,68,80,92C ) and LED settings( 0,3,5,6 )  

gen_subplot_wrapper.m -> Used to validate the input raw images by subplotting the R,G1,G2 and B channels of the raw image
						 across temperatures( 48,56,68,80,92C ) and LED settings( 0,3,5,6 )  

Python Scripts: 
To add noise to the captured raw images at 1280x720 resolution please follow the instructions below:
1. Please run poseScript.py with one argument set to "ORB" or "SIFT" to run using ORB or SIFT algorithm
	Example: python poseScript.py ORB  
2. Before running the poseScript.py please change the following variables inside the script 
	a. Set git_task_accuracy to the path of task_accuracy folder inside the top folder thermal
	b. Modify temp_str variable for the temperatures that you want the script to run 

poseScript.py ---> Top level python script which contain calls to classes 
				   1. Denoises the images collected for the same lighting and distance combination
				   2. Adds noise to the denoised raw image across temperautures 44,56,68,80 and 92C 
                   3. Computes keypoint detectors and descriptors for 4k resolution reference image
				   4. Generates translational and rotational vectors using ORB/SIFT for every noisy image 

GenerateNoisyImage.py  -----> Adds noise to the raw images collected from the sensor. This involves 
						   	  addition of hot pixels, using guassian random distribution to generate new pixels

deNoiseImageSet.py ---------> Denoises all the raw images collected for a lighting and distance combination

MarkerDetectionAndPose.py --> Computes translational and rotational vectors using ORB/SIFT 
                              for a raw image on which noise models are applied 


 
