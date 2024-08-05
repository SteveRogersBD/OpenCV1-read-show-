import cv2 as cv
import numpy as np
import os

# Load the image
img = cv.imread('cap.jpg')

# Resize the image
re_img = cv.resize(img, (300, 300))

# Horizontally stack three copies of the resized image
h = np.hstack((re_img, re_img, re_img))
v=np.vstack((h,h,h))
# Display the horizontally stacked image
#cv.imshow('Captain 1', v)

# Wait for a key press
key = cv.waitKey(0)

# Check if the key pressed is '0'
if key == ord('0'):
    # Destroy the 'Captain 1' window
    cv.destroyWindow('Captain 1')
listName = os.listdir("D:\\Research\\imageReadandWrite\\pics")
for name in listName:
    path="D:\\Research\\imageReadandWrite\\pics"
    image = path+"\\"+name
    img=cv.imread(image)
    img=cv.resize(img,(300,300))
    cv.imshow("Picture",img)
    cv.waitKey(5000)
# The remaining windows (if any) will be destroyed upon another key press
cv.destroyAllWindows()
