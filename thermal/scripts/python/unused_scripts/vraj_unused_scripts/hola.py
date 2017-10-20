import cv2

img=cv2.imread('stones_highres.jpg')
cv2.circle(img,(img.shape[1]/2,img.shape[0]/2),20,(255,0,0),40)
cv2.imshow('img',img)
cv2.imwrite('highres.jpg',img)
cv2.waitKey(0)