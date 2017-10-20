To generate the noise models from the raw image data 
collected from the image sensor matlab scripts are used

Directory Structure:
exp_data  --------> Raw Image Data
proc_data --------> Results after processing the Raw Image Data
scripts/matlab ---> Matlab scripts  
scripts/python ---> Python scripts to measure task accuracy
task_accuracy ----> Raw Image data used to measure task accuracy

Matlab Scripts: 

mean_var_changed.m --->  calculate mean,standard deviation for 32ms_4X configuration of the image sensor 
						 across temperatures( 48,56,68,80,92C ) and LED settings( 0,3,5,6 )  


hot_pixels_calc.m ---->  Measure hot pixels for 32ms_4X configuration of the image sensor 
						 across temperatures( 48,56,68,80,92C ) and LED settings( 0,3,5,6 )  

gen_subplot_wrapper.m -> Used to validate the input raw images by subplotting the R,G1,G2 and B channels of the raw image
						 across temperatures( 48,56,68,80,92C ) and LED settings( 0,3,5,6 )  

Python Scripts: 
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


 
