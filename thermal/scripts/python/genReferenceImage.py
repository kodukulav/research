import cv2
import numpy as np

# Reference image class
class ReferenceImage:
    # Function generate keypoint descriptors
    def generate_kp_desc(self,numFeatures,algo):

        img1 = cv2.imread('./input_images/highres.jpg',0)    # queryImage
        img1.dtype

        # Camera params
        cx = img1.shape[1]/2
        cy = img1.shape[0]/2
        fx = cx * 1.73
        fy = cx * 1.73

        # fx = 1800
        # fy = 1800
        # cx = 375
        # cy = 260

        cameraParams = np.zeros((3, 3), np.float32)

        cameraParams[0][0] = fx
        cameraParams[0][2] = cx
        cameraParams[1][1] = fy
        cameraParams[1][2] = cy
        cameraParams[2][2] = 1

        if algo == "SIFT":
            sift = cv2.xfeatures2d.SIFT_create(nfeatures=numFeatures)
            #print 'REFERENCE IMAGE ',algo

        if algo == "ORB":
            sift = cv2.ORB_create(nfeatures=numFeatures)
            #print 'REFERENCE IMAGE ',algo

        keypointsReference = sift.detect(img1, None)
        keypointsReference, descriptorsReference = sift.compute(img1, keypointsReference)

        heightforImage = 25
        num_kp = len(keypointsReference)
        print "Num_Kp",num_kp
        points3D = np.empty((num_kp, 1, 3), np.float32)

        count = 0

        for kp in enumerate(keypointsReference):
            x = kp[1].pt[0]
            y = kp[1].pt[1]
            Z = 0
            X = (1.00 * heightforImage / fx) * (x-cx )
            Y = (1.00 * heightforImage / fy) * (y-cy )
            pt3d = np.zeros((1, 3), np.float32)
            pt3d[0][0] = X
            pt3d[0][1] = Y
            pt3d[0][2] = Z
            points3D[count] = pt3d
            count += 1


        return keypointsReference,descriptorsReference,cameraParams,points3D


