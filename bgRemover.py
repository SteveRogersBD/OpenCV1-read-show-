import cv2 as cv
sub_m=cv.createBackgroundSubtractorMOG2()
vdo=cv.VideoCapture("D:\\Research\\imageReadandWrite\\video.mp4")
while True:
    r,frame=vdo.read()
    if r==True:
        frame=cv.resize(frame,(500,380))
        sub_v=sub_m.apply(frame)
        cv.imshow('org',frame)
        cv.imshow('sub',sub_v)
        if cv.waitKey(25) & 0xFF==ord('q'):
            break
    else: break
vdo.release()
cv.destroyAllWindows()
