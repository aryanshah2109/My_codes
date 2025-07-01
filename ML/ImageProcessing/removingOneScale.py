import cv2
import numpy as np

img = cv2.imread(r'AIML\ML\ImageProcessing\Images\image1.jpeg')

cv2.imshow('window',img)

cv2.waitKey(0)

img[:,:,0] = 0    # removing blue part from BGR
cv2.imshow('window2',img)
cv2.waitKey(0)

img[:,:,1] = 0    # removing green part from BGR
cv2.imshow('window3',img)
cv2.waitKey(0)

img[:,:,2] = 0    # removing red part from BGR
cv2.imshow('window4',img)
cv2.waitKey(0)


