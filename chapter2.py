import cv2
import numpy as np

img = cv2.imread("resources/shoe2.jpg")
kernel = np.ones((5, 5), np.uint8)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblue = cv2.GaussianBlur(img, (3,3),0)
imgcanny = cv2.Canny(img, 150, 200)
imgdialation = cv2.dilate(imgcanny,kernel,iterations=1)
imgEroded = cv2.erode(imgdialation,kernel,iterations=1)
# cv2.imshow("output", imggray)
# cv2.imshow("output1", imgblue)
cv2.imshow("output2", imgcanny)
cv2.imshow("output3", imgdialation)
cv2.imshow("output4", imgEroded)
cv2.waitKey(0)