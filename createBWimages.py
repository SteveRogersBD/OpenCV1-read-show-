import numpy as np
import cv2 as cv
b_img=np.zeros((500,500,3),np.uint8)*255
w_img=np.ones((500,500,3),np.uint8)*255
cv.imshow('bimg',b_img)
cv.imshow('wimg',w_img)
cv.waitKey(0)
cv.destroyAllWindows()