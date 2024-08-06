import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('cap.jpg')

# Resize the image to 300x300 pixels
img = cv.resize(img, (300, 300))

# Apply Gaussian Blur to the image
# Gaussian Blur helps to smooth the image by reducing noise
g = cv.GaussianBlur(img, (7, 7), 0)

# Apply Median Blur to the image
# Median Blur helps to remove noise while preserving edges
m = cv.medianBlur(img, 5)

# Apply Bilateral Filter to the image
# Bilateral Filter helps to smooth the image while preserving edges
b = cv.bilateralFilter(img, 9, 100, 100)

# Horizontally stack the original image, Gaussian blur, Median blur, and Bilateral filter results
h = np.hstack((img, g, m, b))

# Add a constant border around the original image
# The border is 10 pixels wide on all sides with a constant color (black in this case)
img1 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=0)

# Resize the bordered image to 300x300 pixels
img1 = cv.resize(img1, (300, 300))

# Display the bordered image
cv.imshow('win2', img1)

# Save the horizontally stacked images (original, Gaussian, Median, Bilateral) to a file
cv.imwrite('blur.jpg', h)

# Display the horizontally stacked images
cv.imshow('img', h)

# Wait for a key press indefinitely or for a specified amount of time
cv.waitKey(0)

# Destroy all created windows
cv.destroyAllWindows()
