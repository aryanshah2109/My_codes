import cv2
import numpy as np

img = cv2.imread(r"D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img1.jpeg")
print(img)
print(type(img))
print(img.shape)

cv2.imshow("mywindow",img)
cv2.waitKey(0)