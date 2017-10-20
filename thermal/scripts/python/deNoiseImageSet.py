import numpy as np
import os

# deNoise Image Set
class deNoiseImageSet:
    fixed_width = 1280
    fixed_heigth = 720
    total_pixels = fixed_width * fixed_heigth

    def gen_denoised_image(self,input_imgset_path):

        # Grab all the files in input image set path specified
        all_files = [x for x in os.listdir(input_imgset_path)]

        denoise_img = np.zeros((self.fixed_heigth,self.fixed_width) , dtype='uint8')

        for file in range(0,len(all_files),1):
            all_files[file] = input_imgset_path+all_files[file]
            with open(all_files[file], "rb") as f:
                print "operating on ",all_files[file]
                bayer_img = np.fromstring(f.read(), dtype='uint8')+0.0
                # The raw images that we receive have 922158 bytes in them
                # We need to pick only 921600 bytes corresponding to 921600 pixels
                # Those extra bytes have the metadata about the raw image
                # For example exposure time,analog gain etc...
                # In our case we chose the first 921600 bytes as the image data
                bayer_img = bayer_img[0:self.total_pixels:1]

                bayer_img = np.reshape(bayer_img,(self.fixed_heigth,self.fixed_width))
                # print bayer_img.shape
                bayer_img = (bayer_img/len(all_files))
                denoise_img = denoise_img + bayer_img

        return denoise_img