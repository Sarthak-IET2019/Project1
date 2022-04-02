import cv2 as cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)


myColors = [[0,86,164,179,211,255],
            [161,48,164,179,121,255]
            ]

myColorValues = [[0,0,255],
                 [102,0,204]
                 ]

myPoints = []





def findcolor(img, myColors, myColorValues):

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        x, y = getcontours(mask)

        cv2.circle(imgresult, (x, y), 15, myColorValues[count], cv2.FILLED)


        if x!= 0 and y!= 0:
            newpoints.append([x, y, count])

        count += 1

    return newpoints

def getcontours(img):
    area = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h =0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>500:

            cv2.drawContours(imgresult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            x,y,w,h = cv2.boundingRect(approx)

    return x+w//2, y

def drawoncanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgresult, (point[0],point[1] ), 15, myColorValues[point[2]], cv2.FILLED)



while True:
    success, img = cap.read()
    imgresult= img.copy()

    newpoints = findcolor(img, myColors, myColorValues)
    if len(newpoints)!=0:
        for newp in newpoints:
            myPoints.append(newp)

    if len(myPoints)!=0:
        drawoncanvas(myPoints,myColorValues)

    cv2.imshow("video", imgresult)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break


