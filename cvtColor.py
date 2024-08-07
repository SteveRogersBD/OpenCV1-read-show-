import cv2 as cv
img=cv.imread('cap.jpg')
img=cv.resize(img,(500,500))
# img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
new=img[50:550,100:400] #[y1:y2,x1:x2]
cv.imshow('img',new)
cv.waitKey(0)
cv.destroyAllWindows()