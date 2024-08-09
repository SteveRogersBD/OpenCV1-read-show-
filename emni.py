import numpy as np
import cv2 as cv
img = cv.imread('sudoku.jpg')
img=cv.resize(img,(500,500))
gry=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
can=cv.Canny(gry,10,200)
lines=cv.HoughLinesP(can,1,np.pi/180,200,minLineLength=180,maxLineGap=100)

for i in lines:
    x1,y1,x2,y2 = i[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),4)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()