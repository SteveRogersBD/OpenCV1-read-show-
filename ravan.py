import cv2 as cv

# Read the image from file
img = cv.imread('editcap.jpg')

# Resize the image to (300, 500) dimensions
img = cv.resize(img, (300, 500))

# Extract a portion of the image (a region with height 51 and width 40)
head_img = img[63:114, 155:195]

# Place the extracted portion into a different region of the resized image
# The target region is the same height but a wider width (80 pixels)
img[63:114, 195:235] = head_img

# Display the modified image
cv.imshow('img', img)

# Wait indefinitely for a key press
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()
