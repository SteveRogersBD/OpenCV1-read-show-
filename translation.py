import cv2 as cv
import numpy as np

# Read and resize the image
img = cv.imread('cap.jpg')
img = cv.resize(img, (500, 500))

# Define the transformation matrix
m = np.float32([[1, 0, 100], [0, 1, 50]])
new_img=cv.warpAffine(img,m,(500,500))
# Display the image
cv.imshow('img', new_img)
cv.waitKey(0)
cv.destroyAllWindows()
