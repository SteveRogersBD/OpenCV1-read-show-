import cv2 as cv
import numpy as np
img=cv.imread('bw.jpg')
img=cv.resize(img,(300,300))
m=np.ones((15,15),np.uint8)
e=cv.erode(img,m,iterations=1)
d=cv.dilate(img,m,iterations=1)
cv.imshow('org',img)
cv.imshow('erode',e)
cv.imshow('dilate',d)
cv.waitKey(0)
cv.destroyAllWindows()