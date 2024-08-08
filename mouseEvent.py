import cv2 as cv
import numpy as np
def function(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(white, (x, y), 4, (0, 0, 255), 4)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(white,(x,y),(x+20,y+20),(255,0,0),4)

white=np.ones((500,500,3),np.uint8)*255
cv.namedWindow('Drawing')
cv.setMouseCallback('Drawing',function)
while True:
    cv.imshow('Drawing',white)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
# cv.imshow('test',white)
# cv.waitKey(0)
cv.destroyAllWindows()