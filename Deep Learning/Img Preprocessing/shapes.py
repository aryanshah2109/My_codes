import cv2
import numpy as np

img = cv2.imread(r'D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img5.jpg')

# use thickness = -1 for getting colored and filled shape
 

cv2.rectangle(img,pt1=(100,100),pt2=(500,300),color=(0,255,0),thickness=10)
cv2.circle(img,center=(300,450),radius=100,thickness=10,color=(255,255,0))
cv2.line(img,pt1=(50,50),pt2=(300,300),thickness=10,color=(0,0,255))
cv2.putText(img,text="Hello",org=(100,100),fontScale=3,color=(0,255,255),thickness=10,lineType=cv2.LINE_AA,fontFace=cv2.FONT_HERSHEY_COMPLEX)

cv2.imshow('window',img)
cv2.waitKey(0)