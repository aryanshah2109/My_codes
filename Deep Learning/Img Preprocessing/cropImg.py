import cv2
import numpy as np

img = cv2.imread(r'D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img6.jpeg')
img_reshaped = cv2.resize(img,(400,400))

img_cropped = img_reshaped[100:300,100:300]

cv2.imshow("window",img_reshaped)
cv2.waitKey(0)

cv2.imshow("window",img_cropped)
cv2.waitKey(0)

# saving img
cv2.imwrite(r'D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\cropped_img.jpg',img_cropped)



