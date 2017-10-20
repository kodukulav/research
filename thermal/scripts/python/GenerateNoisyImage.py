import cv2
import numpy as np
import rawpy
import imageio
import random
from Noise_Adder import transform_RG1G2B


class GenerateNoisyImage:

    fixed_width = 1280
    fixed_heigth = 720
    total_pixels = fixed_width * fixed_heigth

    def generate_noisy_image (self, input_denoised_mat, temperature, output_file ):

        # DEBUG CODE
        # git_task_accuracy = 'C:/Users/Sai/Desktop/thermal/task_accuracy'
        # filename = git_task_accuracy + '/test_acc.raw'

        # Instantiate the class object
        noisy_RG1G2B = transform_RG1G2B()

        bayer_img = input_denoised_mat
        print 'Casual check', bayer_img.shape

        # This function used to take a raw image file as input
        # But once the de-noising of the images came into play the coded was not needed
        # This was because the denoising function returns a numpy array instead of a raw image
        '''
        with open(input_file, "rb") as f:
            bayer_img = np.fromstring(f.read(), dtype='uint8')
            bayer_img = bayer_img[0:self.total_pixels:1]
            #print bayer_img.shape
            bayer_img = np.reshape(bayer_img,(self.fixed_heigth,self.fixed_width))
        
        #raw_image = raw.raw_image(filename)
        '''


        # Get the image height and width into two variables
        height,width = bayer_img.shape

        #print height
        # Grab the red, green and blue parts of an image
        red_part    = bayer_img[0::2, 0::2]
        green1_part = bayer_img[0::2, 1::2]
        green2_part = bayer_img[1::2, 0::2]
        blue_part   = bayer_img[1::2, 1::2]

        # Provide the unique string to add configuration,LED setting and temperature specific noise
        unique_string = '32ms_4X_LED_Setting_0,3,5,6_temp_'+temperature


        # Transform the red,green and blue matrices obtained
        # Pass a string indicating the array being passed
        # Let's name them 'r', 'g1', 'g2' and 'b'
        red_npart,green1_npart,green2_npart,blue_npart = noisy_RG1G2B.add_noise_to_RG1G2B(red_part,green1_part,green2_part,blue_part,unique_string)

        noise_rgb_bayer_img = np.zeros(shape=(height,width))
        rg1_bayer_img = np.zeros(shape=(height/2,width))
        g2b_bayer_img = np.zeros(shape=(height/2,width))

        for i in xrange(width/2):
             inter_rg1_col = np.column_stack((red_npart[:,i],green1_npart[:,i]))
             inter_g2b_col = np.column_stack((green2_npart[:,i], blue_npart[:,i]))

             if ( i == 0):
                 rg1_bayer_img = inter_rg1_col
                 g2b_bayer_img = inter_g2b_col
             else:
                 rg1_bayer_img = np.column_stack((rg1_bayer_img,inter_rg1_col))
                 g2b_bayer_img = np.column_stack((g2b_bayer_img,inter_g2b_col))

        for i in xrange(height/ 2):
            inter_row = np.row_stack((rg1_bayer_img[i, :], g2b_bayer_img[i, :]))
            if (i == 0):
                noise_rgb_bayer_img = inter_row
            else:
                noise_rgb_bayer_img = np.row_stack((noise_rgb_bayer_img, inter_row))

        #print noise_rgb_bayer_img.shape
        #print noise_rgb_bayer_img.dtype
        print bayer_img.dtype


        colour = cv2.cvtColor(noise_rgb_bayer_img.astype('uint8'), cv2.COLOR_BAYER_BG2BGR)

        # print colour.shape

        imageio.imsave(output_file+temperature+'.bmp', colour)


        # print cv2.__version__


