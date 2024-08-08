import cv2 as cv
import numpy as np
img = cv.imread('resized.jpg')
img = cv.resize(img,(500,500))
cv.circle(img,(10,10),4,(0,0,255),-1)
cv.circle(img,(10,490),4,(0,0,255),-1)
cv.circle(img,(490,10),4,(0,0,255),-1)
cv.circle(img,(490,490),4,(0,0,255),-1)
src1=np.float32([[10,10],[10,490],[490,10],[490,490]])
dst1=np.float32([[0,0],[0,480],[480,0],[480,480]])
m=cv.getPerspectiveTransform(src1,dst1)

edit=cv.warpPerspective(img,m,(480,480))
cv.imshow('img',edit)
cv.waitKey(0)
cv.destroyAllWindows()