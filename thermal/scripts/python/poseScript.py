from MarkerDetectionAndPose import PoseEstimate
from genReferenceImage import ReferenceImage
#from NameImages import NameImages
#from readRaw import ReadRaw
#from GenerateImages import GenerateImages
#from NoiseAdder import NoiseAdder
from GenerateNoisyImage import GenerateNoisyImage
from deNoiseImageSet import deNoiseImageSet


import os
import csv
import time
import statistics as s
import math as m
import sys

################ INSTANCES OF ALL THE CLASSES #####################

# Create instances of all the classes needed by this code
# Read raw images and store them in .bmp format
#readRaw = ReadRaw()

# Change the name of the images to the following format
# <distance>_<elevation angle>_<2D angle>_<width>_<height>_<sample_number>.<format>
#nameImages=NameImages()

# Add noise to the generated images
# noiseAdder=NoiseAdder()

# Generate the images
# generateImages=GenerateImages()

# Grab a high resolution image
# and generate keypoint descriptors , camera parameters
referenceImage = ReferenceImage()
poseEstimate = PoseEstimate()
# Create a class object here
NoisyImage = GenerateNoisyImage()
deNoisedImage = deNoiseImageSet()

#print "ALGORITHM IS", sys.argv[1]
# Create instances of all the classes needed by this code
################ INSTANCES OF ALL THE CLASSES #####################

#################### DECLARE ALL THE GLOBAL VARIABLES NEEDED ##############
# Generate the raw images from the input files
# Declare all the variables needed by the Noisy image generation class
# File paths
git_task_accuracy = '/home/msb/thermal/task_accuracy'
raw_img  = git_task_accuracy+'/raw_img/'
noisy_img = git_task_accuracy+'/noisy_img/'
# inputImageFolderPath  = git_task_accuracy+'/input_ref_img/'

# Global static variables
listFeatures = [1000]
total_num_of_runs = 50
num_of_rot_trans_vec = 6
temp_str = ['44C','48C','56C','62C','68C','74C','80C','86C','92C']
file_type = 'raw'
fixed_heigth = 720
fixed_width = 1280
algo = sys.argv[1]
output_csv_filename = 'output_'+algo+'.csv'

#print output_csv_filename
# Store the
# 1. average of the runs across temperatures
# 2. error difference between any temperature with 44C
# 3. rotational and translational rms error values across temperatures
trans_rot_vec = {}
trans_rot_vec_avg = {}
err_diff = {}
rot_rms_err = {}
trans_rms_err = {}
denoised_img = []

#################### DECLARE ALL THE GLOBAL VARIABLES NEEDED ##############


################################# OLD VRAJ CODE ##########################
# (keypointsReference,descriptorsReference,cameraParams,points3D) = referenceImage.generate_kp_desc()
# print len(keypointsReference)
# print descriptorsReference.shape

# start_time_for_conversion = time.time()
# all_files = [x for x in os.listdir(inputImageFolderPath)]
# num_files=len(all_files)
# for i in range(0,num_files):
#     readRaw.convertFileFromRaw(inputImageFolderPath+'/'+all_files[i],all_files[i])
# print "Time for Image Conversion {}".format(time.time()-start_time_for_conversion)
#
# nameImages.name_images('OutputImageFolder')
#

# start_time_for_resize = time.time()
# all_files = [x for x in os.listdir(noisy_img)]
# num_files=len(all_files)
# for i in range(0,num_files):
#     generateImages.resize_save(noisy_img+'/'+all_files[i],all_files[i])
# print "Time for Image Resize {}".format(time.time() - start_time_for_resize)

################################# OLD VRAJ CODE ##########################

# Creating a header in the csv file
with open(output_csv_filename, 'wb') as csvfile:
    fieldnames = ['type_of_images','algorithm','numFeatures','width', 'height','distance','run_num','run_time','temperature','rvecs[0]','rvecs[1]','rvecs[2]','tvecs[0]','tvecs[1]','tvecs[2]']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator='\n')
    writer.writeheader()

# Initialise the dictionaries
for x in temp_str:
    trans_rot_vec[x] = [[],[],[],[],[],[]]
    trans_rot_vec_avg[x] = [[],[],[],[],[],[]]
    err_diff[x] = [[],[],[],[],[],[]]


# Start the time when we start computation
start_time_of_program = time.time()

# Grab the directories inside the raw images folder
raw_dir = [x for x in os.listdir(raw_img)]

# Now iterate through each directory that we have got from raw_img path
for dir in raw_dir:

    # For every directory inside raw images directory
    # A denoised numpy array is generated from the set of images
    # That denoised numpy array is given to the noise generation logic
    # to generate noisy images across temperatures
    input_imgset_dir = raw_img+dir+'/'
    denoised_np_arr  = deNoisedImage.gen_denoised_image(input_imgset_dir)

    # A noisy image directory corresponding to the raw image set directory
    noisy_img_dir    = noisy_img + dir + '/'
    if not os.path.exists(noisy_img_dir):
        os.makedirs(noisy_img_dir)

    noisy_img_file = noisy_img_dir+dir+'_'

    # Extract the kind of image from the directory name
    dir_name_split = dir.split('_dist_')
    dist = dir_name_split[0]
    img_kind = dir_name_split[1]

    for run in range(0,total_num_of_runs,1):

        start_time_for_run = time.time()
        # Generate noisy images for a given denoised image from image set
        for temp in temp_str:
            NoisyImage.generate_noisy_image(denoised_np_arr,temp,noisy_img_file)

        for j in range(0,1):
            # Grab the number of features needed for the reference image
            numFeatures = listFeatures[j]

            # Grab all the files from the output image folder
            # Grab all the noisy images
            all_files = [x for x in os.listdir(noisy_img_dir)]
            num_files = len(all_files)
            print (num_files)


            # Compute keypoints and descriptors for the reference image
            (keypointsReference, descriptorsReference, cameraParams, points3D) = referenceImage.generate_kp_desc(numFeatures,algo)

            # Compute the transalational and rotational vectors for the noisy image
            for i in range(0,num_files):
                # Remove the extension from the file and grab the fields from the filename
                filename_no_extension = all_files[i].split('.')[0]
                file_details = filename_no_extension.split('_')
                temperature = file_details[-1]
                # Grab the integer inside the temperature variable
                # For example the code below grabs
                # 44 from 44C
                temp_int_portion = temperature[0]+temperature[1]

                output_file_name = 'out_'+filename_no_extension+'_'+str(run)+'.bmp'

                width  = str(fixed_width)
                height = str(fixed_heigth)
                print (all_files[i])

                # Compute the pose estimate for the noisy image
                res = poseEstimate.calculate_Pose(numFeatures,noisy_img_dir+'/'+all_files[i],'./output_images/'+output_file_name,algo,keypointsReference,descriptorsReference,cameraParams,points3D)

                if (res!=None):
                    for j in range(0,num_of_rot_trans_vec,1):
                        trans_rot_vec[temperature][j].append(res[j])

                run_time = time.time()-start_time_for_run

                # Write out the results of the computed  noisy image to a csv file
                with open(output_csv_filename, 'a') as csvfile:
                    fieldnames = ['type_of_images','algorithm', 'numFeatures',
                                  'width', 'height', 'distance',
                                  'run_num','run_time', 'temperature',
                                  'rvecs[0]', 'rvecs[1]', 'rvecs[2]',
                                  'tvecs[0]', 'tvecs[1]', 'tvecs[2]']

                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator='\n')

                    # In case we don't receive any translational and rotational vectors for the noisy image computed
                    if(res!=None):
                        writer.writerow({'type_of_images':img_kind,'algorithm':"SIFT",'numFeatures':numFeatures,
                                         'width':width, 'height':height,'distance':dist,
                                         'run_num':run+1,'run_time':run_time,'temperature':temp_int_portion,
                                         'rvecs[0]':res[0], 'rvecs[1]':res[1],'rvecs[2]':res[2],
                                         'tvecs[0]':res[3],'tvecs[1]':res[4],'tvecs[2]':res[5]})

                        print (res)

                    else:
                        writer.writerow({'type_of_images':img_kind, 'algorithm':"SIFT",'numFeatures':numFeatures,
                                         'width':width, 'height':height,'distance':dist,
                                         'run_num':run+1,'run_time':run_time,'temperature':temp_int_portion,
                                         'rvecs[0]': str(None), 'rvecs[1]': str(None), 'rvecs[2]': str(None),
                                         'tvecs[0]': str(None), 'tvecs[1]': str(None), 'tvecs[2]': str(None)})


                # print "Time for Image{}".format(time.time() - start_time_for_img)


    '''
    # Take the mean of all the runs
    for x in temp_str:
        for j in range(0,num_of_rot_trans_vec,1):
            # Check if it is an empty list
            if (len(trans_rot_vec[x][j]) == 0):
                trans_rot_vec_avg[x][j] = None
            else:
                trans_rot_vec_avg[x][j] = s.mean(trans_rot_vec[x][j])
            # print x,j,trans_rot_vec_avg[x][j]

    # Compute the error with the reference 44C image
    for j in range(1,len(temp_str),1):
        for k in range(0,num_of_rot_trans_vec,1):
            err_diff[temp_str[j]][k] = trans_rot_vec_avg[temp_str[j]][k] - trans_rot_vec_avg['44C'][k]
            # print 'error', temp_str[j+1],k, err_diff[temp_str[j+1]][k]

    # Calculate the RMS of error
    for j in range(1,len(temp_str),1):
        r1 = err_diff[temp_str[j]][0] * err_diff[temp_str[j]][0]
        r2 = err_diff[temp_str[j]][1] * err_diff[temp_str[j]][1]
        r3 = err_diff[temp_str[j]][2] * err_diff[temp_str[j]][2]
        rot_rms_err[img_kind+'_'+temp_str[j]] = m.sqrt((r1+r2+r3)/3)

        t1 = err_diff[temp_str[j]][3] * err_diff[temp_str[j]][3]
        t2 = err_diff[temp_str[j]][4] * err_diff[temp_str[j]][4]
        t3 = err_diff[temp_str[j]][5] * err_diff[temp_str[j]][5]
        trans_rms_err[img_kind+'_'+temp_str[j]] = m.sqrt(t1+t2+t3/3)

        # print temp_str[j+1], rot_rms_err[img_kind+'_'+temp_str[j + 1]], trans_rms_err[img_kind+'_'+temp_str[j+1]]

with open('final_RMS_Error.csv', 'a') as csvfile:
    fieldnames = ['temperature', 'rotational_RMS_Error', 'translations_RMS_Error']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()

for dir in raw_dir:
    # Extract the kind of image from the directory name
    dir_name_split = dir.split('_dist_')
    img_kind = dir_name_split[1]

    for j in range(1,len(temp_str),1):
        writer.writerow({'temperature': temp_str[j],
                         'rotational_RMS_Error':rot_rms_err[img_kind + '_' + temp_str[j]],
                         'translations_RMS_Error':trans_rms_err[img_kind + '_' + temp_str[j]] })

        print temp_str[j], rot_rms_err[img_kind + '_' + temp_str[j]], trans_rms_err[img_kind + '_' + temp_str[j]]
'''

# Print the time it took to compute the reference image and noisy images
print ("Total Run Time of the program is {}").format(time.time()-start_time_of_program)
