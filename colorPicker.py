import cv2 as cv
import numpy as np

# Create a black image
bimg = np.zeros((500, 500, 3), np.uint8)

# Create a window
cv.namedWindow("color")

# Create trackbars for R, G, B channels
cv.createTrackbar("R", "color", 0, 255, lambda x: None)
cv.createTrackbar("G", "color", 0, 255, lambda x: None)
cv.createTrackbar("B", "color", 0, 255, lambda x: None)

while True:
    # Get the current positions of the trackbars
    r = cv.getTrackbarPos("R", "color")
    g = cv.getTrackbarPos("G", "color")
    b = cv.getTrackbarPos("B", "color")

    # Update the image with the new color
    bimg[:, :] = [b, g, r]

    # Show the image
    cv.imshow("color", bimg)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv.destroyAllWindows()
