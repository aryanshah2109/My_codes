import cv2
import numpy as np

img = cv2.imread(r'D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img2.jpeg')

img_flip0 = cv2.flip(img,0) # horizontal flip
img_flip1 = cv2.flip(img,1) # vertical flip
img_flipminus1 = cv2.flip(img,-1) # horizontal and vertical flip


img_stack = np.hstack((img,img_flip0,img_flip1,img_flipminus1))
cv2.imshow("mywindow",img_stack)
cv2.waitKey(0)
