import cv2 as cv
img1=cv.imread('cap.jpg')
img1=cv.resize(img1,(500,500))
txt=cv.putText(img=img1,text="This is your Captain",org=(52,68),fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=1,color=(0,0,255),thickness=3,lineType=cv.LINE_4)
txt = cv.putText(img=img1,text="This is your Captain",org=(50,70),fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=1,color=(255,0,0),thickness=3,lineType=cv.LINE_4,
               bottomLeftOrigin=False)
#newImg=cv.line(img=txt,pt1=(100,50),pt2=(200,50),color=(0,255,0),
#               thickness=3,lineType=cv.LINE_4)
# newImg2=cv.rectangle(img=txt,pt1=(250,50),pt2=(350,120),color=(0,255,0),
#                thickness=3,lineType=cv.LINE_4)
# newImg2=cv.circle(img=txt,center=(300,100),radius=50,color=(0,0,255),
#                   thickness=5,lineType=cv.LINE_4) #put -1 in thickness to fill the circle

newImg3=cv.ellipse(img=txt,center=(300,100),angle=30,startAngle=0,endAngle=360,axes=(50,100),
                   color=(0,0,255),thickness=3,lineType=cv.LINE_AA)
cv.imshow("Window 1",newImg3)
cv.waitKey(0)
cv.destroyAllWindows()
