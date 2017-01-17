import cv2
import numpy as np
import time
import math
import serial
ser = serial.Serial('COM4', 9600)
cap = cv2.VideoCapture(2)

lower = [60,30,30]
upper = [140,255,255]

lp=[125,30,30]
up=[255,255,255]
resource=[]

cx=[1]
cy=[0]
px=[0]
py=[0]

cap.set(12, 4)
cap.set(10, 0)
cap.set(11, 44)

while True :
    ret, snap = cam.read()
    snap = cv2.GaussianBlur(snap, (5,5),0)
    hsv = cv2.cvtColor(snap, cv2.COLOR_BGR2HSV)

    lower_y = np.array(lowery)
    upper_y = np.array(uppery)
    mask = cv2.inRange(hsv, lower_y, upper_y)
    res = cv2.bitwise_and(snap, snap, mask = mask)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, 1)
    contours, h = cv2.findContours(thresh, 1, 2)

    for cnt in contours :
        if cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 100000 :
            approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
            if len(approx) == 3 :
                cv2.drawContours(snap,[cnt],-1,(255,0,0),2)
            if len(approx) == 4 :
                cv2.drawContours(snap,[cnt],-1,(255,0,0),2)
    cv2.imshow('snap', snap)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
for cnt in contours:
    if cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 10000:
        approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt,True), True)
        if len(approx) == 3:
            yt = yt + [cnt[0]]
        if len(approx) == 4:
            ys = ys + [cnt[0]]

resource = yt + ys

def angle(xp,yp,xb,yb):
    mx=float(xp-xb)
    my=float(yp-yb)
    if mx == 0:
        return 90
    global mtan
    if(mx > 0 and my > 0):
        mtan=math.degrees(math.atan(float(my/mx)))
    elif(my>0 and mx<0):
        mtan=180 + math.degrees(math.atan(float(my/mx)))
    elif(my <0 and mx<0):
        mtan=180+math.degrees(math.atan(float(my/mx)))
    else:
        mtan=360+math.degrees(math.atan(float(my/mx)))
    return mtan
while True :
    ser.write('r')
    time.sleep(0.2)
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (9,9),0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(lower)
    upper_blue = np.array(upper)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,1)
    contours,h = cv2.findContours(thresh,1,2)
    for cnt in contours :
        if cv2.contourArea(cnt) > 1000 and cv2.contourArea(cnt) < 200000 :
            approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
            if len(approx)== 4 :
                if len(approx)== 4:
                    M=cv2.moments(cnt)
                    x=int(M['m10']/M['m00'])
                    y=int(M['m01']/M['m00'])
                    cx = [x]
                    cy = [y]
                    cv2.drawContours(frame,[cnt],-1,(255,0,0),2)

    lowerp = np.array(lp)
    upperp = np.array(up)
    mask1 = cv2.inRange(hsv, lowerp, upperp)
    res1 = cv2.bitwise_and(frame,frame, mask= mask1)

    gray = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,1)
    contours,h = cv2.findContours(thresh,1,2)
    for cnt in contours :
        if cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 300000 :
            approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
            if len(approx)== 4 :
                M=cv2.moments(cnt)
                g=int(M['m10']/M['m00'])
                f=int(M['m01']/M['m00'])
                px = [g]
                py = [f]
                cv2.drawContours(frame,[cnt],-1,(255,255,0),2)
    global xp
    xp=px[-1]
    global yp
    yp=py[-1]
    global xb
    xb=cx[-1]
    global yb
    yb=cy[-1]
    t1 = angle(xp,yp,xb,yb)
    xr=resource[0][0][0]
    yr=resource[0][0][1]
    t2=angle(xr,yr,xb,yb)
    print "marker :",t1
    print "resource :",t2
    cv2.imshow('res',res)
    cv2.imshow('res1',res1)
    cv2.imshow('mask1', mask1)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
ser.close()
