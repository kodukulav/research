import numpy as np
import cv2
import sys, getopt

class PoseEstimate:

    def calculate_Pose(self,numFeatures,inputimage,outputimage,algo,keypointsReference,descriptorsReference,cameraParams,points3D):
        MIN_MATCH_COUNT = 10

        # img1 = cv2.imread('stones.jpg',0)    # queryImage

        # imgColor =cv2.imread('side_img.jpg')
        # img2 = cv2.imread('side_img.jpg',0) # trainIma



        # inputimage = 'img_far.jpg'
        # inputimage='OutputImageFolder/50_0_0_810_1080_2.jpg'
        # inputimage = 'TestNoiseImages/50_0_30_810_1080_2_26.jpg'
        imgColor =cv2.imread(inputimage)
        img2 = cv2.imread(inputimage,0) # trainIma

        cx = img2.shape[1]/2
        cy = img2.shape[0]/2
        fx = cx*1.73
        fy = cx*1.73

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

        # imgColor=cv2.resize(imgColor,(1000,1000))
        # img2 = cv2.resize(img2, (1000, 1000))
        # imgColor = cv2.imread('photo_60_50.jpg')
        # img2 = cv2.imread('photo_60_50.jpg', 0)  # trainIma

        #  instrinsic camera parameters for refernce image
        #imagw size - 750*530
        # fx = 687
        # fy = 647
        # cx = 230
        # cy = 340
        #
        # cameraParams = np.zeros((3,3),np.float32)
        #
        # cameraParams[0][0]=fx
        # cameraParams[0][2]=cx
        # cameraParams[1][1]=fy
        # cameraParams[1][2]=cy
        # cameraParams[2][2]=1
        #
        # sift=cv2.SIFT()
        #
        # keypointsReference = sift.detect(img1,None)
        # keypointsReference, descriptorsReference = sift.compute(img1, keypointsReference)
        #
        # heightforImage = 12
        # num_kp = len(keypointsReference)
        #
        # points3D = np.empty((num_kp,1,3),np.float32)
        #
        # count=0
        # for kp in enumerate(keypointsReference):
        #     x = kp[1].pt[0]
        #     y = kp[1].pt[1]
        #     Z=0
        #     X = (1.00*heightforImage/fx)*(x-cx)
        #     Y = (1.00*heightforImage/fy)*(y-cy)
        #     pt3d= np.zeros((1,3),np.float32)
        #     pt3d[0][0] = X
        #     pt3d[0][1] = Y
        #     pt3d[0][2] = Z
        #     points3D[count]=pt3d
        #     count+=1

        if algo == "SIFT":
            #print 'REFERENCE IMAGE ', algo
            #SIFT Implementation
            sift = cv2.xfeatures2d.SIFT_create(nfeatures=numFeatures)

            keypointsDest = sift.detect(img2,None)
            keypointsDest, descriptorsDest = sift.compute(img2, keypointsDest)

            #taking a flann based matcher
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            # index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6)  # 12 key_size = 12, # 20 multi_probe_level = 1)

            FLANN_INDEX_LSH=6
            # index_params = dict(algorithm=FLANN_INDEX_LSH,
            #                     table_number=10,  # 12
            #                     key_size=10,  # 20
            #                     multi_probe_level=0)  # 2
            search_params = dict(checks = 50)

            # descriptorsReference.astype(np.float32)
            # descriptorsDest.astype(np.float32)

            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(descriptorsDest,descriptorsReference,k=2)
            good = []

            for (m,n) in (matches):
                if m.distance < 0.7*n.distance:
                    good.append(m)



            # drawing matches on

            kp2=[]
            print "Matches",len(good)
            for i in range(0,len(good)):
                idx = good[i].queryIdx
                kp2.append(keypointsDest[idx])

            #SIFT implementation ends

        if algo == "ORB":
            #print 'REFERENCE IMAGE ', algo
            #ORB Implementation
            orb =cv2.ORB_create(nfeatures=numFeatures)
            keypointsDest, descriptorsDest = orb.detectAndCompute(img2, None)

            FLANN_INDEX_LSH = 6
            index_params = dict(algorithm=FLANN_INDEX_LSH,table_number=6,key_size=10, multi_probe_level=2)
            search_params = dict(checks=50)

            descriptorsReference.astype(np.float32)
            descriptorsDest.astype(np.float32)

            flann = cv2.FlannBasedMatcher(index_params, search_params)
            matches = flann.knnMatch(descriptorsDest, descriptorsReference, k=2)
            good = []

            for match in matches:
                try:
                    if(match[0] and match[1]):
                        if match[0].distance < 0.7 * match[1].distance:
                            good.append(match[0])
                except:
                    print "Error"

            # drawing matches on
            # good = [[0, 0] for i in xrange(len(matches))]
            #
            # for i, (m, n) in enumerate(matches):
            #     if m.distance < 0.7 * n.distance:
            #         good[i] = [1, 0]

            kp2 = []
            print "Matches", len(good)
            for i in range(0, len(good)):
                idx = good[i].queryIdx
                kp2.append(keypointsDest[idx])

            #ORB Implementation ends


        # prepare data for findHomography
        src_pts = np.float32([keypointsReference[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypointsDest[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)

        try:
            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        except:
            print "Error"
            return None

        matchesMask = mask.ravel().tolist()

        inliers=[]

        for i in range(0,len(matchesMask)):
            if(matchesMask[i]):
                inliers.append(good[i])

        num_inliers = len(inliers)

        #making a list of corresponding 3D and 2D points

        pnp3d=np.empty((num_inliers,1,3),np.float32)
        pnp2d=np.empty((num_inliers,1,2),np.float32)
        for i in range(0,num_inliers):
            i1=inliers[i].trainIdx
            pnp3d[i]=(points3D[i1])
            i2= inliers[i].queryIdx
            pnp2d[i]=keypointsDest[i2].pt


        dist = np.zeros((5,1),np.float32)



        _, rvecs, tvecs, inliers = cv2.solvePnPRansac(pnp3d, pnp2d, cameraParams, dist)

        axislength=10;
        axis = np.float32([[0,0,0],[axislength,0,0], [0,axislength,0], [0,0,-axislength ]]).reshape(-1,3)
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, cameraParams, dist)

        # cv2.line(imgColor,(200,200) , tuple(imgpts[0].ravel()), (255, 0, 0), 2)
        # cv2.line(imgColor,(200,200) , tuple(imgpts[1].ravel()), (0, 255, 0), 2)
        # cv2.line(imgColor,(200,200) , tuple(imgpts[2].ravel()), (0, 0, 255), 2)

        cv2.line(imgColor,tuple(imgpts[0].ravel()) , tuple(imgpts[1].ravel()), (255, 0, 0), 2)
        cv2.line(imgColor,tuple(imgpts[0].ravel()) , tuple(imgpts[2].ravel()), (0, 255, 0), 2)
        cv2.line(imgColor,tuple(imgpts[0].ravel()) , tuple(imgpts[3].ravel()), (0, 0, 255), 2)


        # return str(rvecs)+str(tvecs)
        # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('img', 1280, 720)
        # cv2.imshow('img',imgColor)
        cv2.imwrite(outputimage,imgColor)
        #cv2.waitKey(0)
        a = [0]*6
        a[0]=rvecs[0][0]*180/3.14
        a[1]=rvecs[1][0]*180/3.14
        a[2]=rvecs[2][0]*180/3.14
        a[3]=tvecs[0][0]
        a[4]=tvecs[1][0]
        a[5]=tvecs[2][0]


        # import math
        # dst,jacobain = cv2.Rodrigues(rvecs)
        # print dst
        # print "x",tvecs[0][0]
        #    print "y", tvecs[2][0]
        # t= math.asin(-dst[0][2])
        # print "t", t
        #
        # rx  = tvecs[2][0]*math.cos((math.pi/2)-t)
        # ry = tvecs[2][0] * math.sin((math.pi / 2) - t)
        # print "rx",rx
        # print "ry",ry

        return a
