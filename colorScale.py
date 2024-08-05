import cv2 as cv
img1=cv.imread('cap.jpg',1)
img2=cv.imread('cap.jpg',0)
img3=cv.imread('cap.jpg',-1)
img1=cv.resize(img1,(300,300))
img2=cv.resize(img2,(300,300))
img3=cv.resize(img3,(300,300))
cv.imshow('win1',img1)
cv.imshow('win2',img2)
cv.imshow('win3',img3)
key=cv.waitKey(0)
if key==ord('0'):
    cv.destroyAllWindows()