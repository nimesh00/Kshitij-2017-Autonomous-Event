import numpy as np
import cv2
#import serial
#ser = serial.Serial('COM4', 9600)

yml = 1
xml = 2
ymu = 3
xmu = 4
resource = [[[487, 363]],[[139, 345]],[[333, 168]],[[133, 166]],[[475, 108]],[[260,  46]],[[487, 363]],[[139, 345]]]
#pink
lp=[125,100,30]
up=[255,255,255]

lbl=[90,80,0]
ubl=[120,255,255]


#yellow
lower = [20,70,30]
upper = [40,255,255]

# brown
lower_brown = [5,150,50]
upper_brown = [28,255,255]

#red
lower_red = [0,100,100]
upper_red = [10,255,255]


#blue
lower_blue = [80,50,50]
upper_blue = [160,255,255]

f = 0
r = 0
cx=[1]
cy=[0]
px=[0]
py=[0]
yt = []
ys = []
bs = []
resources = []
def traverse(tanb, tanr) :
    if (tanr - tanb) > 5 :
        print "move right"
        #ser.write('r')
    elif (tanr - tanb) < -5 :
        print "move left"
        #ser.write('l')
    else :
        print "go straight"
        #ser.write('f')
def retrace(tanb, tanr) :
    f = 1
    if (tanr - tanb) > 5 :
        print "move right"
        #ser.write('r')
    elif (tanr - tanb) < -5 :
        print "move left"
        #ser.write('l')
    else :
        print "go backward"
        #ser.write('b')

    '''
img = cv2.imread('arena1.png')
cv2.imshow('first_capture', img)
#gray = cv2.imread('arena1.png',0)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower1 = np.array(lower)
upper1 = np.array(upper)
mask = cv2.inRange(hsv,lower1,upper1)
res = cv2.bitwise_and(img,img, mask = mask)
gray1 = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray1, 127,255,1)
contours,h = cv2.findContours(thresh,1,2)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
    if len(approx) ==3 :
        yt = yt + [cnt[0]]
        cv2.drawContours(img,[cnt],-1,(0,0,255),2)
    if len(approx) ==4 :
        cv2.drawContours(img,[cnt],-1,(0,255,0),2)
        ys = ys + [cnt[0]]

lower2 = np.array(lower_brown)
upper2 = np.array(upper_brown)
mask1 = cv2.inRange(hsv,lower2,upper2)
res1 = cv2.bitwise_and(img,img, mask = mask1)
gray2 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(mask1, 127,255,1)
contours,h = cv2.findContours(thresh,1,2)
for cnt in contours:
    if cv2.contourArea(cnt) < 300000:        
        approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
        if len(approx) ==4 :
            cv2.drawContours(img,[cnt],-1,(0,255,0),2)
            bs = [cnt[0]]
bsx = bs[0][0][0]
bsy = bs[0][0][1]
'''
cam = cv2.VideoCapture(1)
ret, img = cam.read()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lowery = np.array(lower)
uppery = np.array(upper)
mask = cv2.inRange(hsv, lowery, uppery)
res = cv2.bitwise_and(img, img, mask = mask)
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 1)
contours, h = cv2.findContours(thresh, 1, 2)

for cnt in contours :
    if cv2.contourArea(cnt) < 300000 :
        approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
        if len(approx) == 3 :
            cv2.drawContours(img,[cnt],-1,(255,0,0),2)
            yt = yt + [cnt[0]]
        if len(approx) == 4 :
            cv2.drawContours(img,[cnt],-1,(200,0,150),2)
            ys = ys + [cnt[0]]
resources = ys + yt
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
x1 = bs[0][0][0]
y1 = bs[0][0][1]
for i in range(len(resources)) :
    print "x,y :", resources[i][0][0], resources[i][0][1]
print 'town center : ', x1, y1
resources = yt + ys
collect = len(resources)
collected = 0
r = 0
upper_mark = []
lower_mark = []
while True :
    if r > len(resources):
        break
    ret, frame = cam.read()
    '''
    hsvf = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower3 = np.array(lower_red)
    upper3 = np.array(upper_red)
    maskr = cv2.inRange(hsvf,lower3,upper3)
    resr = cv2.bitwise_and(frame, frame, mask =maskr)
    grayr = cv2.cvtColor(resr, cv2.COLOR_BGR2GRAY)
    ret, threshr = cv2.threshold(grayr,127,255,1)
    contoursr,h  = cv2.findContours(threshr,1,2)
    for cnt1 in contoursr :
        area = cv2.contourArea(cnt1)
        if area < 300000 :
            approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt1,True),True)
            if len(approx) == 4 :
                cv2.drawContours(frame,[cnt1],-1,(255,0,0),2)
                lower_mark = [cnt1[0]]
                xml = lower_mark[0][0][0]
                yml = lower_mark[0][0][1]
    lower4 = np.array(lower_blue)
    upper4 = np.array(upper_blue)
    maskb = cv2.inRange(hsvf, lower4,upper4)
    resb = cv2.bitwise_and(frame, frame, mask = maskb)
    grayb = cv2.cvtColor(resb, cv2.COLOR_BGR2GRAY)
    ret, threshb = cv2.threshold(grayb,127,255,1)
    contoursb,h  = cv2.findContours(threshb,1,2)
    for cnt1 in contoursb :
        area = cv2.contourArea(cnt1)
        if area < 300000:
            approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt1,True),True)
            if len(approx) == 4 :
                cv2.drawContours(frame,[cnt1],-1,(255,0,0),2)
                upper_mark = [cnt1[0]]
                xmu = upper_mark[0][0][0]
                ymu = upper_mark[0][0][1]
                '''
    lowery=np.array(lp)
    uppery=np.array(up)
    mask=cv2.inRange(hsv,lowery,uppery)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,1)
    contours,h=cv2.findContours(thresh,1,2)
    for cnt in contours:
        if cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 30000:
            approx=cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
            if len(approx)== 4:
                M=cv2.moments(cnt)
                x=int(M['m10']/M['m00'])
                y=int(M['m01']/M['m00'])
                cx = [x]
                cy = [y]
                
               
    lower_blue=np.array(lbl)
    upper_blue=np.array(ubl)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,1)
    contours,h=cv2.findContours(thresh,1,2)
    for cnt1 in contours:
        if cv2.contourArea(cnt1) > 10 and cv2.contourArea(cnt1) < 30000:
            approx=cv2.approxPolyDP(cnt1,0.03*cv2.arcLength(cnt1,True),True)
            if len(approx)== 4:
                M=cv2.moments(cnt)
                g=int(M['m10']/M['m00'])
                f=int(M['m01']/M['m00'])
                px = [g]
                py = [f]
    x2 = resources[r][0][0]
    y2 = resources[r][0][1]
    pt = (x1, y1)
    q = (x2, y2)
    if((x2-x1)==0):
            tempr=0
    else:
        a1=(y2-y1)/float(x2-x1)
        a1=("%.2f" %a1)

    x2=range(x2-3,x2+2)
    y2=range(y2-3,y2+2)

    x1=range(x1-3,x1+2)
    y1=range(y1-3,y1+2)
        
    #BOT 
    x11=cx[-1]
    y11=cy[-1]
    x21= px[-1]
    y21=py[-1]

    #slopes
        
    if(x21-x11==0):
        tempb=0
    else:
        a2=(y21-y11)/float(x21-x11)
        a2=("%.2f" %a2)
        
    pt=(x11,y11)
    q=(x21,y21)
    cv2.line(frame,pt,q,(0,0,255))
        
    cv2.imshow('frame',frame)
    #tanb = (py - cy)/(float)(px - cx)
    #tanr = (resource[r][0][1] - bsy)/(resource[r][0][0] - bsx)
    print a2, a1
    if (resource[r][0][0] - px) < 10 and (resource[r][0][1] - py) < 10:
        print "blink"
        f = 1;
    elif f == 0 :
        traverse(a2, a1)
    elif f == 1 :
        retrace(a2, a1)
        if px < bsx and py < bsy :
            f = 0
            r += 1

    cv2.imshow('brown',res1)
    cv2.imshow('yellow',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
#ser.close()
