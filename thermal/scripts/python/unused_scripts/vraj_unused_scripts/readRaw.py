import cv2
import numpy as np
from PIL import Image
from rawkit.raw import Raw
import imageio
import rawpy
import os


class ReadRaw:

    def convertFileFromRaw(self,filepath,filename):

        filename_no_extension=filename.split('.')[0]
        raw = rawpy.imread(filepath)
        rgb = raw.postprocess(no_auto_bright=True,use_auto_wb =True,gamma=None)
        imageio.imwrite('OutputImageFolder/'+filename_no_extension+'.bmp', rgb)


