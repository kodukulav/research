import os
class NameImages:


#images will be stored as d_phi_theta_wid_height_number
    file_arr = []
    file_arr.append('50_0_0_3024_4032_1.jpg')
    file_arr.append('50_0_0_3024_4032_2.jpg')
    file_arr.append('50_0_0_3024_4032_3.jpg')

    file_arr.append('50_0_15_3024_4032_1.jpg')
    file_arr.append('50_0_15_3024_4032_2.jpg')
    file_arr.append('50_0_15_3024_4032_3.jpg')

    file_arr.append('50_0_30_3024_4032_1.jpg')
    file_arr.append('50_0_30_3024_4032_2.jpg')
    file_arr.append('50_0_30_3024_4032_3.jpg')

    file_arr.append('50_0_45_3024_4032_1.jpg')
    file_arr.append('50_0_45_3024_4032_2.jpg')
    file_arr.append('50_0_45_3024_4032_3.jpg')

    file_arr.append('50_0_60_3024_4032_1.jpg')
    file_arr.append('50_0_60_3024_4032_2.jpg')
    file_arr.append('50_0_60_3024_4032_3.jpg')

    file_arr.append('50_0_-15_3024_4032_1.jpg')
    file_arr.append('50_0_-15_3024_4032_2.jpg')
    file_arr.append('50_0_-15_3024_4032_3.jpg')

    file_arr.append('50_0_-30_3024_4032_1.jpg')
    file_arr.append('50_0_-30_3024_4032_2.jpg')
    file_arr.append('50_0_-30_3024_4032_3.jpg')

    file_arr.append('50_0_-45_3024_4032_1.jpg')
    file_arr.append('50_0_-45_3024_4032_2.jpg')
    file_arr.append('50_0_-45_3024_4032_3.jpg')

    file_arr.append('50_0_-60_3024_4032_1.jpg')
    file_arr.append('50_0_-60_3024_4032_2.jpg')
    file_arr.append('50_0_-60_3024_4032_3.jpg')
    # file_arr.append('50_0_-30_3024_4032_1.dng')
    # file_arr.append('50_0_-30_3024_4032_2.dng')
    # file_arr.append('50_-30_0_3024_4032_1.dng')
    # file_arr.append('50_-30_0_3024_4032_2.dng')
    # file_arr.append('50_30_30_3024_4032_1.dng')
    # file_arr.append('50_30_30_3024_4032_2.dng')
    # file_arr.append('50_0_0_3024_4032_1.dng')
    # file_arr.append('50_0_0_3024_4032_2.dng')
    # file_arr.append('100_0_30_3024_4032_1.dng')
    # file_arr.append('100_0_30_3024_4032_2.dng')
    # file_arr.append('100_0_-30_3024_4032_1.dng')
    # file_arr.append('100_0_-30_3024_4032_2.dng')
    # file_arr.append('100_-30_0_3024_4032_1.dng')
    # file_arr.append('100_-30_0_3024_4032_2.dng')
    # file_arr.append('100_30_30_3024_4032_1.dng')
    # file_arr.append('100_30_30_3024_4032_2.dng')

    def name_images(self,folderpath):

        arr_txt = [x for x in os.listdir(folderpath)]
        print arr_txt
        num_files=len(arr_txt)
        for i in range(0,num_files):
            os.rename(folderpath+"/"+arr_txt[i],folderpath+"/"+self.file_arr[i])
