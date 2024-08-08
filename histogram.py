import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Create blank white and black images
blank_w = np.ones((500, 500, 3), np.uint8) * 255
blank_b = np.zeros((500, 500, 3), np.uint8) * 255

# Read and resize images
dark = cv.imread('D:\\Research\\imageReadandWrite\\histoPics\\Darkgray.jpg', 0)
dark = cv.resize(dark, (200, 300))

grey = cv.imread('D:\\Research\\imageReadandWrite\\histoPics\\gray.jpg', 0)
grey = cv.resize(grey, (200, 300))

white = cv.imread('D:\\Research\\imageReadandWrite\\histoPics\\brightgray.jpg', 0)
white = cv.resize(white, (200, 300))

# Calculate histograms for each image
hist1 = cv.calcHist([dark], [0], None, [256], [0, 256])
hist2 = cv.calcHist([grey], [0], None, [256], [0, 256])
hist3 = cv.calcHist([white], [0], None, [256], [0, 256])
hist_blank_b = cv.calcHist([blank_b], [0], None, [256], [0, 256])

# Merge dark, grey, and white images horizontally
merged_images = np.hstack((dark, grey, white))

# Display merged images
cv.imshow('merged', merged_images)

# Plot histograms
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(hist1)
plt.title('Histogram of Dark Gray Image')

plt.subplot(3, 1, 2)
plt.plot(hist2)
plt.title('Histogram of Gray Image')

plt.subplot(3, 1, 3)
plt.plot(hist3)
plt.title('Histogram of Bright Gray Image')

plt.tight_layout()
plt.show()

# Display blank images
cv.imshow('blank_w', blank_w)
cv.imshow('blank_b', blank_b)

# Wait and close windows
cv.waitKey(0)
cv.destroyAllWindows()
