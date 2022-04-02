import cv2
import numpy as np

img = np.zeros((512, 512,3),np.uint8)
# print(img)
# img[:]= 255,0,0

cv2.line(img, (0,0), (300,300),(0,255,0),2)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(200,200),30,(255,255,0),4)
cv2.putText(img, "opencv", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),4)
cv2.imshow("output", img)
cv2.waitKey(0)