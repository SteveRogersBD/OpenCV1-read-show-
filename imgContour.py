import cv2 as cv
import numpy as np

# Read and resize the image
img = cv.imread('D:\\Research\\imageReadandWrite\\pics\\the_daily_star.png')
img = cv.resize(img, (500, 500))

# Convert the image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply binary thresholding to the grayscale image
_, thr = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
white=np.ones((500,500,3),np.uint8)*255
new_img = cv.drawContours(white, contours, -1, (0, 0, 255), 3)

# Display the image with contours
cv.imshow('img', new_img)
cv.waitKey(0)
cv.destroyAllWindows()
