import cv2 as cv
import numpy as np

# Read and resize the image
img = cv.imread('shapes.jpg')
img = cv.resize(img, (600, 600))

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply binary thresholding to the grayscale image
_, thr = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

# Find contours in the thresholded image
cnt, hir = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Draw the contour (only once outside the loop)
cv.drawContours(img, cnt, -1, (0, 0, 255), 3)
# Initialize a list to store contour areas
ar = []
# Process each contour
for c in cnt:
    m = cv.moments(c)
    # Calculate the centroid of the contour
    if m['m00'] != 0: #if area is not zero then proceed
        x = int(m['m10'] / m['m00'])
        y = int(m['m01'] / m['m00'])
        # Draw the centroid
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)  # Increased radius to 5
        # Calculate and store the contour area
        a = cv.contourArea(c)
        ar.append(a)
        ep=0.01*cv.arcLength(c, True)
        d=cv.approxPolyDP(c,ep,True)
        h=cv.convexHull(d)
        x,y,w,h=cv.boundingRect(h)
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Print contour areas
print(ar)

# Display the image with contours and centroids
cv.imshow('img', img)
cv.imshow('gray', thr)
cv.waitKey(0)
cv.destroyAllWindows()
