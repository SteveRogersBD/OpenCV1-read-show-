import cv2 as cv
img=cv.imread('cap.jpg')
img=cv.resize(img,(500,500))
img1=cv.Canny(img,100,200,apertureSize=5,L2gradient=True)
# cv.imshow('img',img)
# cv.imshow('img1',img1)

#rotation
w,h=img.shape[0],img.shape[1]
m=cv.getRotationMatrix2D((w/2,h/2),30,1)
new_img=cv.warpAffine(img,m,(500,500))
cv.imshow('img',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
