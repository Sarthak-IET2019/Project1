import cv2
import numpy as np


img = cv2.imread("resources/shoe2.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))

imgCropped = img[0:400, 200:400]#height comes first then the width

cv2.imshow("output", img)
# cv2.imshow("output2", imgResize)
cv2.imshow("output3", imgCropped)
cv2.waitKey(0)