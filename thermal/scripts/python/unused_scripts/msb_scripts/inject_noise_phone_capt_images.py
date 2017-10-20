import cv2
import numpy as np
from PIL import Image
from rawkit.raw import Raw

import rawpy
import imageio
import random
from noise_adder import transform_RG1G2B

noisy_RG1G2B = transform_RG1G2B()

filename = 'C:\Users\Sai\Downloads\IMG_20171006_140246.dng'


with rawpy.imread(filename) as raw:
    #raw = rawpy.imread(filename)
    bayer_img = raw.raw_image
   # bayer_img = bayer_img
    bayer_img = bayer_img/4


    # Get the image height and width into two variables
    height,width = bayer_img.shape

    print height
    # Grab the red, green and blue parts of an image
    red_part    = bayer_img[0::2, 0::2]
    green1_part = bayer_img[0::2, 1::2]
    green2_part = bayer_img[1::2, 0::2]
    blue_part   = bayer_img[1::2, 1::2]

    # Provide the unique string to add configuration,LED setting and temperature specific noise
    unique_string = '32ms_4X_LED_Setting_0,3,5,6_temp_48C'

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

    #bayer_img = np.copy(noise_rgb_bayer_img)
    raw_img = raw.raw_image
    raw_img[:,:]=noise_rgb_bayer_img[:,:]

    rgb = raw.postprocess(output_bps=8)

    imageio.imsave( 'C:\Users\Sai\Downloads\IMG_20171004_164502.png', rgb)


    # imageio.imsave('C:\Users\Sai\Downloads\IMG_20171004_164502.dng', noise_rgb_bayer_img)

    #print random.sample([1,2,3],2)

    for i in xrange(10):
        if (i == 1):
            print np.mean(red_part)
            print np.mean(red_npart)
            print red_npart.shape

    b = 0.5*3
    print int((1/2)*3)



    #print r10bit.dtype
    # print r10bit.item(1,10)
    # rgb = raw.postprocess(output_bps=8)

    # print rgb.item(1,10,0)
    # print rgb.item(1,10,1)
    # print rgb.item(1,10,2)

    #print rgb.shape
    #print rgb.dtype
    #print rgb.item(1,10,1)
    # res = cv2.resize(rgb, (720,1280), interpolation = cv2.INTER_AREA)
    #print res.shape
    # imageio.imsave( 'C:\Users\Sai\Downloads\IMG_20171004_164502.bmp', res)

    #imageio.imsave( 'C:\Users\Sai\Downloads\IMG_20171004_164502.png', rgb)

    print cv2.__version__

    #raw_image = Raw(filename)
    #buffered_image = np.array(raw_image.to_buffer())
    #image = Image.frombytes('RGB', (raw_image.metadata.width, raw_image.metadata.height), buffered_image)
    #image.save('C:\Users\Sai\Downloads\IMG_20171004_164502.png', format='png')

    # Read the image from the filepath
    #imgOriginal = cv2.imread('C:\Users\Sai\Downloads\IMG_20171004_164502.dng')
    #height, width, channels = imgOriginal.shape
    #print height, width, channels
    #print imgOriginal.shape


    #img2 = cv2.resize(imgOriginal, (1280,720));#, interpolation=cv2.INTER_LINEAR)
