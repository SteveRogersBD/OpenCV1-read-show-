import cv2 as cv
import numpy as np

img=cv.imread('sudoku.jpg')
img=cv.resize(img,(500,500))
gry=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edg=cv.Canny(gry,20,250)
l=cv.HoughLinesP(edg,1,np.pi/180,200,minLineLength=180,maxLineGap=100)
print(l)
for i in l:
    x1,y1,x2,y2=i[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()