import cv2 as cv
import numpy as np

# Open a connection to the default webcam (index 0)
cap = cv.VideoCapture(0)

# Create a window to display results
cv.namedWindow("demo")


# Function for trackbar change (not used here but required)
def ani(x):
    pass


# Create trackbars for lower and upper HSV values
cv.createTrackbar("lb", "demo", 0, 255, ani)
cv.createTrackbar("lg", "demo", 0, 255, ani)
cv.createTrackbar("lr", "demo", 0, 255, ani)

cv.createTrackbar("ub", "demo", 255, 255, ani)
cv.createTrackbar("ug", "demo", 255, 255, ani)
cv.createTrackbar("ur", "demo", 255, 255, ani)

while cap.isOpened():
    # Read a frame from the webcam
    r, frame = cap.read()

    # Check if the frame was read successfully
    if r:
        # Convert the frame to HSV color space
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Get trackbar positions for lower bounds
        Lb = cv.getTrackbarPos("lb", "demo")
        Lg = cv.getTrackbarPos("lg", "demo")
        Lr = cv.getTrackbarPos("lr", "demo")

        # Get trackbar positions for upper bounds
        Ub = cv.getTrackbarPos("ub", "demo")
        Ug = cv.getTrackbarPos("ug", "demo")
        Ur = cv.getTrackbarPos("ur", "demo")

        # Create the lower and upper bounds for the HSV mask
        lo = np.array([Lb, Lg, Lr])
        hi = np.array([Ub, Ug, Ur])

        # Create a mask using the HSV range
        mask = cv.inRange(hsv, lo, hi)

        # Apply the mask to the frame
        res = cv.bitwise_and(hsv, hsv, mask=mask)

        # Show the result
        cv.imshow("demo", res)

        # Exit the loop if 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
