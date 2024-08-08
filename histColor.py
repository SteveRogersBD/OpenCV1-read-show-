import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
img=cv.imread('cap.jpg')
img=cv.resize(img,(500,500))

b,g,r=cv.split(img)

# Calculate histograms for each image
# hist1 = cv.calcHist([b], [0], None,
#                     [256], [0, 256])
# hist2 = cv.calcHist([g], [0], None,
#                     [256], [0, 256])
# hist3 = cv.calcHist([r], [0], None,
#                     [256], [0, 256])
plt.hist(b.ravel(),256,[0,256],color="blue")
plt.hist(g.ravel(),256,[0,256],color="green")
plt.hist(r.ravel(),256,[0,256],color="red")
plt.show()
# Plot histograms
# plt.figure()
# plt.subplot(3, 1, 1)
# plt.plot(hist1)
# plt.title('Histogram of Blue Image')
#
# plt.subplot(3, 1, 2)
# plt.plot(hist2)
# plt.title('Histogram of Green Image')
#
# plt.subplot(3, 1, 3)
# plt.plot(hist3)
# plt.title('Histogram of Red Image')

# plt.tight_layout()
# plt.show()
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

# Wait and close windows
cv.waitKey(0)
cv.destroyAllWindows()
