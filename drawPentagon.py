import cv2 as cv
import numpy as np
old_img = cv.imread('cap.jpg')
old_img=cv.resize(old_img,(500,500))
points = np.array([[[450, 250], [360, 374], [240, 374], [150, 250], [240, 126]]],
                  dtype=np.int32)

new_img=cv.polylines(img=old_img,pts=points,
                     isClosed=True,color=(255,0,0),thickness=1,lineType=cv.LINE_AA)
cv.imshow('Win1',new_img)
cv.waitKey(0)
cv.destroyAllWindows()