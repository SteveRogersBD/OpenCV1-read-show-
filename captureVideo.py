import cv2 as cv
cap=cv.VideoCapture(0)
while True:
    r,frame=cap.read()
    if r==True:
        frame=cv.resize(frame,(640,480))
        cv.imshow('frame',frame)
        if cv.waitKey(25) & 0xff ==ord('p'):
            break
    else: break
cap.release()
cv.destroyAllWindows()