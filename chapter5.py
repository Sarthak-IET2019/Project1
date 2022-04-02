import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")


width = 250
height = 350
pts1 = np.float32([[243,380],[407,375],[412,580],[235,580]])
pts2 = np.float32([[0,0],[width,0],[width,height],[height,0]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width,height))
cv2.imshow("output", img)
cv2.imshow("output1", imgOutput)
cv2.waitKey(0)