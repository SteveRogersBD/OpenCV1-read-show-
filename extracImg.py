import cv2 as cv
vdo=cv.VideoCapture("video.mp4")
c=0
while vdo.isOpened():
    r,frame=vdo.read()
    if r==True:
        frame=cv.resize(frame,(500,500))
        path = f"D:\\Research\\imageReadandWrite\\frames\\frame{c}.png"
        cv.imwrite(path,frame)
        cv.imshow('frame',frame)
        c = c + 1
        if cv.waitKey(25) & 0xff==ord('q'):
            break
    else: break
vdo.release()
cv.destroyAllWindows()