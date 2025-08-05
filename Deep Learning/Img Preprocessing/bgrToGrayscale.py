import cv2
import numpy as np

img = cv2.imread(r"D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img2.jpeg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("myWindow",img)
cv2.waitKey(0)

cv2.imshow("mywindow",img_gray)

cv2.waitKey(0)