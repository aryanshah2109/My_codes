import cv2
import numpy as np

# Reading an image
img = cv2.imread(r'AIML\ML\ImageProcessing\Images\image1.jpeg')
print(type(img))
print(img.shape)

new_img = cv2.resize(img,(800,500))
cv2.imshow('window',new_img)

 
cv2.waitKey(0)

# converting a rgb image to grey scale

img_bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('window2',img_bw)

cv2.waitKey(0)