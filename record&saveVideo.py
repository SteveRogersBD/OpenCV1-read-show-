import cv2 as cv

# Open a connection to the default webcam (index 0)
cap = cv.VideoCapture(0)

# Define the codec for video encoding and create a VideoWriter object
f = cv.VideoWriter_fourcc(*"mp4v")  # Codec for MPEG-4 video encoding
out = cv.VideoWriter('output.mp4', f, 40, (500, 500), 0)
# Output video file, 40 FPS, resolution 500x500, grayscale (1 stands for colorful which is
# also the default val)

while True:
    # Read a frame from the webcam
    r, frame = cap.read()

    # Check if the frame was read successfully
    if r == True:
        # Resize the frame to 500x500 pixels
        frame = cv.resize(frame, (500, 500))

        # Convert the frame to grayscale
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Flip the frame horizontally (mirror effect)
        frame = cv.flip(frame, 1)

        # Write the processed frame to the output video file
        out.write(frame)

        # Display the frame in a window titled 'frame'
        cv.imshow('frame', frame)

        # Check for user input to exit (press 'q' to quit)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv.destroyAllWindows()
