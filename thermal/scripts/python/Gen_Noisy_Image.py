import cv2
import numpy as np
import rawpy
import imageio
import random
from noise_adder import transform_RG1G2B


noisy_RG1G2B = transform_RG1G2B()



filename = 'C:\Users\Sai\Downloads\Test_acc'
#filename = 'C:/Users/Sai/Desktop/thermal/exp_data/32ms_4x_3_r9_20170920_1144/9'



def generate_noisy_image ( filename, temperature ):
    fixed_width  = 1280
    fixed_heigth = 720
    total_pixels = fixed_width*fixed_heigth
    bayer_img = []
    noise_rgb_bayer_img = []

    with open(filename, "rb") as f:
        bayer_img = np.fromstring(f.read(), dtype='uint8')
        bayer_img = bayer_img[0:total_pixels:1]
        print bayer_img.shape
        bayer_img = np.reshape(bayer_img,(fixed_heigth,fixed_width))

    #raw_image = raw.raw_image(filename)
    print bayer_img.shape

    # Get the image height and width into two variables
    height,width = bayer_img.shape

    print height
    # Grab the red, green and blue parts of an image
    red_part    = bayer_img[0::2, 0::2]
    green1_part = bayer_img[0::2, 1::2]
    green2_part = bayer_img[1::2, 0::2]
    blue_part   = bayer_img[1::2, 1::2]

    # Provide the unique string to add configuration,LED setting and temperature specific noise
    unique_string = '32ms_4X_LED_Setting_0,3,5,6_temp_'+temperature+'C'

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

    print noise_rgb_bayer_img.shape
    print noise_rgb_bayer_img.dtype
    print bayer_img.dtype


    colour = cv2.cvtColor(noise_rgb_bayer_img.astype('uint8'), cv2.COLOR_BAYER_BG2BGR)

    print colour.shape

    imageio.imsave('C:\Users\Sai\Downloads\Noisy_image'+temperature+'C.bmp', colour)


    print cv2.__version__

generate_noisy_image(filename,'44')
generate_noisy_image(filename,'48')
generate_noisy_image(filename,'56')
generate_noisy_image(filename,'68')
generate_noisy_image(filename,'80')
generate_noisy_image(filename,'92')
