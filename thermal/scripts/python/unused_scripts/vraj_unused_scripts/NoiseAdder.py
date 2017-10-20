import cv2
import numpy as np
import random


class NoiseAdder:
    def generateImagesWithNoise(self,folderpath,filename,sd):
        img=cv2.imread(folderpath)

        rows=img.shape[0]
        cols=img.shape[1]

        img_new =np.zeros((rows,cols,3),np.float32)

        for i in range(0,rows):
            for j in range(0,cols):

                pixel  = img[i,j]
                # print pixel
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]

                slope_r=1;
                slope_g = 1;
                slope_b = 1;

                intercept_r = 0
                intercept_g = 0
                intercept_b = 0

                '''
                if 0<=red<76:
                    slope_r = 1.00
                    intercept_r = 0.00

                if 76<=red<83:
                    slope_r = 2.43
                    intercept_r = -108.57

                if 83<=red<90:
                    slope_r = 23.14
                    intercept_r = -1827.86

                if 90<=red<=255:
                    slope_r = 0.00
                    intercept_r = 255.00

                if 0<=green<86:
                    slope_g = 1.02
                    intercept_g = 0.00

                if 86<=green<119:
                    slope_g = 5.06
                    intercept_g = -347.21

                if 119<=green<=255:
                    slope_g = 0.00
                    intercept_g = 255.00

                if 0<=blue<73:
                    slope_b = 1.03
                    intercept_b = 0.00

                if 73<=blue<90:
                    slope_b = 10.59
                    intercept_b = -697.94

                if 90<=blue<=255:
                    slope_b = 0.00
                    intercept_b = 255.00
                '''
                random_red = random.gauss((red * slope_r)+intercept_r,sd)
                random_green = random.gauss((green * slope_g) + intercept_g,sd)
                random_blue = random.gauss((blue * slope_b) + intercept_b,sd)

                img_new[i,j]=np.array([random_red,random_green,random_blue])

        cv2.imwrite('TestNoiseImages/'+'50_0_30_810_1080_2_'+str(sd)+'.jpg',img_new)
