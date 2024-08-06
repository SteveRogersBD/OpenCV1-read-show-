import cv2 as cv
import numpy as np
img1=cv.imread('bw.jpg')
img1=cv.resize(img1,(300,300))
img2=cv.imread('bw2.jpg')
img2=cv.resize(img2,(300,300))
# img3=np.bitwise_and(img1,img2)
# img3=np.bitwise_or(img1,img2)
img3=np.bitwise_xor(img1,img2)
img4=np.bitwise_not(img1)
h=np.hstack((img1,img2,img3))
cv.imshow('h',img4)
cv.waitKey(0)
cv.destroyAllWindows()
