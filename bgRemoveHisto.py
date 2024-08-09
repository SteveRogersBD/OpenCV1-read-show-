import cv2 as cv

# Read and preprocess images
img1 = cv.imread('shield.jpg')
img1 = cv.resize(img1, (500, 200))
hsv1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)

img2 = cv.imread('green.jpg')
img2 = cv.resize(img2, (500, 200))
hsv2 = cv.cvtColor(img2, cv.COLOR_BGR2HSV)

# Calculate the histogram from hsv1 image
# Use appropriate bin counts and ranges
hist1 = cv.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Perform back projection on hsv2 using hist1
mask = cv.calcBackProject([hsv1], [0, 1], hist1, [0, 180, 0, 256], 1)

# Apply the mask to img2
res = cv.bitwise_and(img2, img2, mask=mask)

ker=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
mask=cv.filter2D(mask,-1,ker)
_,thr=cv.threshold(mask,200,255,cv.THRESH_BINARY)
mask=cv.merge((mask,mask,mask))
res=cv.bitwise_or(img1,mask)
# Display results
cv.imshow('Original Image', img2)
cv.imshow('Back Projection Result', res)
cv.waitKey(0)
cv.destroyAllWindows()
