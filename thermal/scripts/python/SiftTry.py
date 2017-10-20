# import cv2
import cv2
import numpy as np


img1=cv2.imread('vuforia_stones.jpg',0)
imgColor = cv2.imread('vuforia_stones.jpg')
sift = cv2.SIFT()
keypointsReference = sift.detect(img1, None)
keypointsReference, descriptorsReference = sift.compute(img1, keypointsReference)

imgColor=cv2.drawKeypoints(img1,keypointsReference,(0,255,0))

print len(keypointsReference)
cv2.imshow('img',imgColor)
cv2.waitKey(0)