import cv2
import numpy as np
import time
import RPi.GPIO as gp

motpin0 = 22
motpin1 = 23
motpin2 = 24
motpin3 = 25
gp.setmode(gp.BCM)
gp.setup(motpin0,gp.OUT)
gp.setup(motpin1,gp.OUT)
gp.setup(motpin2,gp.OUT)
gp.setup(motpin3,gp.OUT)

cap = cv2.VideoCapture(0)
lower = [20,100,30]
upper = [40,255,255]

while True :
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(lower)
    upper_blue = np.array(upper)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,1)
    contours,h = cv2.findContours(thresh,1,2)
    for cnt in contours :
        if cv2.contourArea > 1000 :
            approx = cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
            if len(approx)==3 :
                print "triangle"
                cv2.drawContours(res,[cnt],-1,(255,0,0),2)
                gp.output(motpin0,gp.HIGH)
                gp.output(motpin1,gp.LOW)
                gp.output(motpin2,gp.HIGH)
                gp.output(motpin3,gp.LOW)
                time.sleep(2)
            else :
                gp.output(motpin0,gp.LOW)
                gp.output(motpin1,gp.LOW)
                gp.output(motpin2,gp.LOW)
                gp.output(motpin3,gp.LOW)
                
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
gp.cleanup()
