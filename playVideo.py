import cv2 as cv

# Open a video file
cap = cv.VideoCapture('video.mp4')

# Check if the video file is opened successfully
while cap.isOpened():
    # Read a frame from the video
    r, frame = cap.read()

    # Check if the frame is read correctly
    if r == True:
        # Resize the frame to 640x480 pixels
        frame = cv.resize(frame, (640, 480))

        # Display the resized frame in a window named 'video'
        cv.imshow('video', frame)

        # Check if the 'p' key is pressed
        if cv.waitKey(60) & 0xFF == ord('p'):
            # Break the loop if 'p' is pressed
            break
    else:
        # If no frame is read (end of video), exit the loop
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv.destroyAllWindows()
