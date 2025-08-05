import cv2
import numpy as np

img = cv2.imread(r'D:\CODING_CODES\AIML\Deep Learning\Img Preprocessing\Images\img6.jpeg')

cv2.imshow("mywindow",img)
cv2.waitKey(0)

img_play = np.hstack((img[:,:,0],img[:,:,1],img[:,:,2]))

cv2.imshow("mywindow",img_play)
cv2.waitKey(0)



