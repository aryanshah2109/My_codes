import cv2
import numpy as np

img = cv2.imread(r"D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img6.jpeg")

print(img.shape)

img_resized = cv2.resize(img,(500,500))

print(img_resized.shape)


cv2.imshow("mywindow",img)
cv2.waitKey(0)

cv2.imshow("mywindow",img_resized)
cv2.waitKey(0)