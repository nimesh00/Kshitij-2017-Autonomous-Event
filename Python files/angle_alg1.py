import cv2
import numpy as np
import serial
import time
import math

ser = serial.Serial('COM8',9600)

yt = []
ys = []
resources = []
cx=[1]
cy=[0]
px=[0]
py=[0]
mx = 0
my = 0

lowery = [20,10,30]
uppery = [40,255,255]

# brown
lower_brown = [5,150,50]
upper_brown = [28,255,255]

lower = [60,10,30]
upper = [140,255,255]

lp=[125,10,30]
up=[255,255,255]

cam = cv2.VideoCapture(2)
cam.set(12, 4)
cam.set(10, 0)
cam.set(11, 44)

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
'''
lowerb = np.array(lower_brown)
upperb = np.array(upper_brown)
mask = cv2.inRange(hsv, lowerb, upperb)
res = cv2.bitwise_and(img, img, mask = mask)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(mask, 127, 255, 1)
contours, h = cv2.findContours(thresh, 1, 2)
for cnt in contours :
    if cv2.contourArea(cnt) < 300000 :
        approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True),True)
        if len(approx) == 4 :
            cv2.drawContours(img,[cnt],-1,(255,0,255),2)
            bs =  bs + [cnt[0]]

'''
resources = yt + ys
for r in range(len(resources)):
    print "x,y : ",resources[r][0][0], resources[r][0][1]
r = 0
def marker():
    cx=[0]
    cy=[0]
    px=[0]
    py=[0]
    ret, frame = cam.read()
    cv2.imshow('initial', frame)
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
    cv2.imshow('frame', frame)
    global xp
    xp=px[-1]
    global yp
    yp=py[-1]
    global xb
    xb=cx[-1]
    global yb
    yb=cy[-1]
    #global mx
    #mx = int(cx[-1] + px[-1])/2
    #global my
    #my = int(cy[-1] + py[-1])/2
    
#bsx = bs[0][0][0]
#bsy = bs[0][0][1]
'''
def angle(c1,c2,c3,c4):
    global slp = float(c4 - c2)/(c3 - c1)
    ang = math.atan(slp)
    ang = (ang * 180)/3.14
    if xp < xb and yp > yb :
        ang = ang + 180
    elif xp > xb and yp > yb :
        ang = ang + 180
    return ang
'''
def angle(xp,yp,xb,yb):
    dx=float(xp-xb)
    dy=float(yp-yb)
    if dx == 0:
        return 90
    global mtan
    if(dx > 0 and dy > 0):
        mtan=math.degrees(math.atan(float(dy/dx)))
    elif(dy>0 and dx<0):
        mtan=180 + math.degrees(math.atan(float(dy/dx)))
    elif(dy <0 and dx<0):
        mtan=180+math.degrees(math.atan(float(dy/dx)))
    else:
        mtan=360+math.degrees(math.atan(float(dy/dx)))
    print mtan
    return mtan
def distance(x1,y1,x2,y2) :
    dist = math.sqrt((x1- x2)**2 + (y1 - y2)**2)
    return dist
while True :
    x1 = int(resources[1][0][0])
    y1 = int(resources[1][0][1])
    marker()
    #print cx, cy
    #print px, py
    xp = px[-1]
    yp = py[-1]
    xb = cx[-1]
    yb = cy[-1]
    marker()
    mx=int(xp+xb)/2
    my=int(yp+yb)/2
    t1 = angle(x1, y1,mx, my)
    t2 = angle(xp, yp, xb, yb)
    print t1, t2
    diff=t1- t2
    tol = 10
    if(diff <180):
        pass
    else:
        diff=0-(360-diff)
    if(diff > - 180):
        pass
    else:
        diff=360+diff
    print "differnce", diff  
    if diff > tol :
        ser.write('l')
        print "l"
        time.sleep(0.1)
    elif diff < -tol :
        print "r"
        ser.write('r')
        time.sleep(0.1)
    else :
        print "f"
        ser.write('f')
        time.sleep(0.1)
    if distance(x1, y1, mx, my) < 15 :
        ser.write('s')
        time.sleep(3)
        print "stop"
        ser.write('o')
        print "blink"
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()
ser.close()
