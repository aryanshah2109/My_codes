import cv2
import numpy as np

img = cv2.imread(r'AIML\ML\ImageProcessing\Images\image2.jpeg')

imgBlue = img[:,:,0]
imgRed = img[:,:,1]
imgGreen = img[:,:,2]

new_img = np.hstack((imgBlue,imgGreen,imgRed))

new_img = cv2.resize(new_img,(800,500))
cv2.imshow('window',new_img)
cv2.waitKey(0)


