import cv2
import numpy as np

sizeList = []
# sizeList.append((1440, 1920))
# sizeList.append((960, 1280))
# sizeList.append((720, 960))
# sizeList.append((480, 640))
# sizeList.append((240, 320))

# sizeList array has lot of resolutions
sizeList.append((3024,4032))
sizeList.append((3000,4000))
sizeList.append((2904,3872))
sizeList.append((2730,3640))
sizeList.append((2580,3440))
sizeList.append((2430,3240))
sizeList.append((2250,3000))
sizeList.append((2100,2800))
sizeList.append((2040,2720))
sizeList.append((1950,2600))
sizeList.append((1860,2480))
sizeList.append((1650,2200))
sizeList.append((1500,2000))
sizeList.append((1440,1920))
sizeList.append((1350,1800))
sizeList.append((1200,1600))
sizeList.append((1080,1440))
sizeList.append((960,1280))
sizeList.append((810,1080))
sizeList.append((720,960))
sizeList.append((675,900))
sizeList.append((660,880))
sizeList.append((600,800))
sizeList.append((570,760))
sizeList.append((540,720))
sizeList.append((510,680))
sizeList.append((480,640))
sizeList.append((450,600))
sizeList.append((435,580))
sizeList.append((405,540))
sizeList.append((375,500))
sizeList.append((360,480))
sizeList.append((330,440))
sizeList.append((300,400))
sizeList.append((270,360))
sizeList.append((240,320))
sizeList.append((225,300))
sizeList.append((210,280))
sizeList.append((189,252))
sizeList.append((165,220))
sizeList.append((150,200))
sizeList.append((135,180))
sizeList.append((120,160))
sizeList.append((114,152))
sizeList.append((105,140))
sizeList.append((90,120))
sizeList.append((75,100))
sizeList.append((60,80))
sizeList.append((48,64))
sizeList.append((36,48))
sizeList.append((24,32))


# class to generate images
class GenerateImages:

    # Function which looks to resize the images
    def resize_save(self, filepath, filename):

        # Read the image from the filepath
        imgOriginal = cv2.imread(filepath)

        # Grab the fields of the file name
        filename_no_extension = filename.split('.')[0]
        file_details = filename_no_extension.split('_')

        #fields of file name
        dist   = file_details[0]
        phi    = file_details[1]
        theta  = file_details[2]
        width  = file_details[3]
        height = file_details[4]
        num    = file_details[5]

        # sizeList has different resolutions
        num_len = len(sizeList)


        for i in range(0, num_len):
            newWidth = sizeList[i][0]
            newHeight = sizeList[i][1]
            newFileName = str(dist) + '_' + str(phi) + '_' + str(theta) + '_' + str(newWidth) + '_' + str(newHeight) + '_' + str(num)
            img2 = cv2.resize(imgOriginal, sizeList[i], interpolation=cv2.INTER_LINEAR)
            cv2.imwrite('OutputImageFolder/' + newFileName + '.jpg', img2)

