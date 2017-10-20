import cv2
import numpy as np
import random
# Import classes to return RGB slopes, intercepts, stddevs and hot pixels
# at a specific configuration, LED setting and temperature
from noise_models.mean_intercepts import RGB_intercepts_sensor_config_LED_Setting_temp
from noise_models.mean_slopes import RGB_slopes_sensor_config_LED_Setting_temp
from noise_models.stddev import RGB_stddev_sensor_config_LED_Setting_temp
from noise_models.hot_pixels import RGB_hot_pixels_sensor_config_LED_Setting_temp



class transform_RG1G2B:

    # Instantiate the class objects
    mean_intercepts = RGB_intercepts_sensor_config_LED_Setting_temp()
    mean_slopes = RGB_slopes_sensor_config_LED_Setting_temp()
    stddev = RGB_stddev_sensor_config_LED_Setting_temp()
    hot_pixels = RGB_hot_pixels_sensor_config_LED_Setting_temp()

    rgb_int = {}
    rgb_slp = {}
    rgb_sd  = {}
    rgb_hp  = {}

    def add_noise_to_RG1G2B(self,Rmat,G1mat,G2mat,Bmat,unique_string):
        self.rgb_int['Red'],self.rgb_int['Green'],self.rgb_int['Blue'] = self.mean_intercepts.ret_RGB_intercept_at_config_LED_Setting_temp(unique_string)
        self.rgb_slp['Red'],self.rgb_slp['Green'],self.rgb_slp['Blue'] = self.mean_slopes.ret_RGB_slope_at_config_LED_Setting_temp(unique_string)
        self.rgb_sd['Red'],self.rgb_sd['Green'],self.rgb_sd['Blue']    = self.stddev.ret_RGB_stddev_at_config_LED_Setting_temp(unique_string)
        self.rgb_hp['Red'],self.rgb_hp['Green'],self.rgb_hp['Blue']    = self.hot_pixels.ret_RGB_hot_pixels_at_config_LED_Setting_temp(unique_string)

        #Rmat_trans  = random.gauss((Rmat * self.rgb_slp['Red'])   + self.rgb_int['Red'],self.rgb_sd['Red'])
        #G1mat_trans = random.gauss((G1mat * self.rgb_slp['Green']) + self.rgb_int['Green'], self.rgb_sd['Green'])
        #G2mat_trans = random.gauss((G2mat * self.rgb_slp['Green']) + self.rgb_int['Green'], self.rgb_sd['Green'])
        #Bmat_trans  = random.gauss((Bmat * self.rgb_slp['Blue'])  + self.rgb_int['Blue'], self.rgb_sd['Blue'])

        Rmat_trans  = self.random_guass_randint(Rmat,  self.rgb_slp['Red'],   self.rgb_int['Red'],   self.rgb_sd['Red'])
        G1mat_trans = self.random_guass_randint(G1mat, self.rgb_slp['Green'], self.rgb_int['Green'], self.rgb_sd['Green'])
        G2mat_trans = self.random_guass_randint(G2mat, self.rgb_slp['Green'], self.rgb_int['Green'], self.rgb_sd['Green'])
        Bmat_trans  = self.random_guass_randint(Bmat,  self.rgb_slp['Blue'],  self.rgb_int['Blue'],  self.rgb_sd['Blue'])

        Rmat_trans  = self.insert_hot_pixels(Rmat_trans,  self.rgb_hp['Red'])
        G1mat_trans = self.insert_hot_pixels(G1mat_trans, self.rgb_hp['Green']/2)
        G2mat_trans = self.insert_hot_pixels(G2mat_trans, self.rgb_hp['Green']/2)
        Bmat_trans  = self.insert_hot_pixels(Bmat_trans,  self.rgb_hp['Blue'])

        return Rmat_trans,G1mat_trans,G2mat_trans,Bmat_trans


    def insert_hot_pixels(self, RGBmat, num_hot_pixels ):

        # Collect the heigth and width of the R,G1,G2 and B numpy arrays
        heigth,width = RGBmat.shape
        # print heigth, width
        rand_y = list(range(heigth))
        rand_x = list(range(width))

        # 1280x720 resolution image
        fixed_image_sensor_value = 921600 #1280*720

        # 4032x3024 resolution image
        # fixed_samsung_galaxy_value = 12192768 #4032*3024

        # Scaling the number of hot pixels obtained in 1280x720 image to 4032x3024 based image
        #float_new_hot_pixels = (num_hot_pixels*fixed_samsung_galaxy_value)/fixed_image_sensor_value
        #new_hot_pixels = int(float_new_hot_pixels)

        # The number of hot pixels received is only valid for 1280x720
        for i in xrange(int(num_hot_pixels)):
            # Pick a random x,y co-ordinate
            y = random.sample(rand_y,1)
            x = random.sample(rand_x,1)

            # Hot pixels logic
            # Pick a random value between the maximum pixel value of 255 and
            # the hot pixel start value decided by the hot pixel logic
            # The start value is set as mean(whole image) + 30
            mean = np.mean(RGBmat)
            mean = int(mean)
            hot_pixel_start_val = mean + 30
            pixel_overwrite_val = 255
            if ( hot_pixel_start_val < 255):
                pixel_overwrite_val = random.randint(hot_pixel_start_val,255)

            # print pixel_overwrite_val
            # Insert the randomised pixel value at the random x,y coordinate chosen
            RGBmat[y,x] = pixel_overwrite_val

        return RGBmat


    def random_guass_randint(self, mat, slope, intercept, stddev):

        mat_trans = ((mat * slope) + intercept)
        #print mat_trans.dtype
        h, w = mat.shape
        zero_mat = mat_trans*0
        std_mat = zero_mat + stddev
        gaussian = np.random.normal(zero_mat,std_mat)

        mat_trans = mat_trans + gaussian


        '''
        print mat_trans[120,54]
        print mat_trans[125, 53]
        print mat_trans[255, 255]

        print "mat trans"
        print intercept
        '''

        mat_trans[mat_trans<0]=0
        mat_trans[mat_trans>255]=255
        return mat_trans