#threshold is a technique used to remove foreground from bg
import cv2 as cv
img=cv.imread('cap.jpg')
img=cv.resize(img,(500,500))
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,h=cv.threshold(img,15,170,cv.THRESH_BINARY)
#15: The threshold value. Pixels with intensity values greater than or equal
# to this value are set to the maximum value
_,h2=cv.threshold(img,100,170,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow('img',img)
cv.imshow('img2',h)
cv.imshow('img3',h2)
cv.waitKey(0)
cv.destroyAllWindows()