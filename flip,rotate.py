import cv2 as cv
img = cv.imread('cap.jpg')
img=cv.resize(img,(500,500))
img1=cv.flip(img,1)
img2=cv.flip(img,0)
img3=cv.flip(img,-1)
img4=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
img5=cv.transpose(img)
cv.imshow('img',img5)

cv.waitKey(0)
cv.destroyAllWindows()