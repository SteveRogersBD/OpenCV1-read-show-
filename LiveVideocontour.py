import cv2 as cv
import numpy as np

# Create a window and trackbars for HSV threshold adjustments
cv.namedWindow('Video')


def nothing(x):
    pass


# Create trackbars for HSV color filtering
cv.createTrackbar('th', 'Video', 0, 255, nothing)
cv.createTrackbar('lb', 'Video', 0, 255, nothing)
cv.createTrackbar('lg', 'Video', 0, 255, nothing)
cv.createTrackbar('lr', 'Video', 0, 255, nothing)
cv.createTrackbar('ub', 'Video', 255, 255, nothing)
cv.createTrackbar('ug', 'Video', 255, 255, nothing)
cv.createTrackbar('ur', 'Video', 255, 255, nothing)

# Open video capture
cap = cv.VideoCapture(0)

while cap.isOpened():
    r, frame = cap.read()
    if r:
        # Get trackbar positions
        thr = cv.getTrackbarPos('th', 'Video')
        Lb = cv.getTrackbarPos('lb', 'Video')
        Lg = cv.getTrackbarPos('lg', 'Video')
        Lr = cv.getTrackbarPos('lr', 'Video')
        Ub = cv.getTrackbarPos('ub', 'Video')
        Ug = cv.getTrackbarPos('ug', 'Video')
        Ur = cv.getTrackbarPos('ur', 'Video')

        # Define HSV color range
        lower = np.array([Lb, Lg, Lr])
        upper = np.array([Ub, Ug, Ur])

        # Resize and flip the frame
        frame = cv.resize(frame, (500, 350))
        frame = cv.flip(frame, 1)

        # Convert to HSV color space
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Create a mask for the color range
        m = cv.inRange(hsv, lower, upper)

        # Apply the mask to get the result
        res = cv.bitwise_and(frame, frame, mask=m)

        # Apply binary thresholding to the mask
        _, thi = cv.threshold(m, thr, 255, cv.THRESH_BINARY)

        # Find contours
        contours, _ = cv.findContours(thi, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Draw contours on the result image
        cv.drawContours(frame, contours, -1, (0, 0, 255), 3)

        # Display images
        cv.imshow('thr', thi)
        cv.imshow('Result', res)
        cv.imshow('hsv', hsv)
        cv.imshow('original', frame)

        # Exit on 'q' key press
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release video capture and close all windows
cap.release()
cv.destroyAllWindows()
