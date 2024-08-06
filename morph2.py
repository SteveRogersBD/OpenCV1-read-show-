import numpy as np
import cv2 as cv
img=cv.imread('bw.jpg')
img=cv.resize(img,(300,300))
k=np.ones((10,10),np.uint8)
opening=cv.morphologyEx(img,cv.MORPH_OPEN,k,iterations=3) #removes white noises
closing=cv.morphologyEx(img,cv.MORPH_CLOSE,k,iterations=3) #removes black noises
gradient=cv.morphologyEx(img,cv.MORPH_GRADIENT,k,iterations=1)
tophead=cv.morphologyEx(img,cv.MORPH_TOPHAT,k,iterations=1)
blackhead=cv.morphologyEx(img,cv.MORPH_BLACKHAT,k,iterations=1)
#cv.imshow('img',img)
cv.imshow('opening',opening)
cv.imshow('closing',closing)
cv.imshow('gradient',gradient)
cv.imshow('tophead',tophead)
cv.imshow('blackhead',blackhead)
cv.waitKey(0)
cv.destroyAllWindows()