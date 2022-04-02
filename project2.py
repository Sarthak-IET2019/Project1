import cv2 as cv2
import numpy as np






cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
count = 0
minarea = 500
color= (255,0,255)
nPlateCascade = cv2.CascadeClassifier("resources/haarcascade_russian_plate_number.xml")

while True:
    success, img = cap.read()
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = nPlateCascade.detectMultiScale(imggray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minarea:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
         cv2.putText(img, "detected", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
         imgroi = img[y:y+h, x:x+w]
         cv2.imshow("roi", imgroi)





    cv2.imshow("video", img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        cv2.imwrite("resources/scanned/Noplate_"+str(count)+".jpg",imgroi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"scan succesful",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("video",img)
        cv2.waitKey(500)
        count += 1



