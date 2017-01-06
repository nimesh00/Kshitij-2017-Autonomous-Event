import numpy as np
import cv2

lower = [20,100,30]
upper = [40,255,255]

lower_brown = [5,150,50]
upper_brown = [28,255,255]

#red
lower_red = [0,100,100]
upper_red = [10,255,255]


#blue
lower_blue = [80,50,50]
upper_blue = [160,255,255]

f = 0
yt = []
ys = []
bs = []
resources = []
def traverse(tanb, tanr) :
    if (tanr - tanb) > 5 :
        print "move right"
    elif (tanr - tanb) < -5 :
        print "move left"
    else :
        print "go straight"
def retrace(tanb, tanr) :
    f = 1
    if (tanr - tanb) > 5 :
        print "move right"
    elif (tanr - tanb) < -5 :
        print "move left"
    else :
        print "go backward"

    
img = cv2.imread('arena1.png')
gray = cv2.imread('arena1.png',0)
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
ret, thresh = cv2.threshold(gray2, 127,255,1)
contours,h = cv2.findContours(thresh,1,2)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
    if len(approx) ==4 :
        cv2.drawContours(img,[cnt],-1,(0,255,0),2)
        bs = [cnt[0]]


for i in range(len(yt)) :
    print 'x,y for triangles',i + 1,' is ', yt[i][0][0], yt[i][0][1]
for j in range(len(ys)) :
    print 'x,y for squares',j + 1,' is ', ys[j][0][0], ys[j][0][1]
print 'town center : ',bs[0][0][0],bs[0][0][1]
bsx = bs[0][0][0]
bsy = bs[0][0][1]
resources = yt + ys
collect = len(resources)
collected = 0
r = 0;
upper_mark = []
lower_mark = []
cam = cv2.VideoCapture(1)

while True :
    if r > len(resources):
        break
    ret, frame = cam.read()
    hsvf = cv2.cvtColor(frame, cv3.COLOR_BGR2HSV)
    lower3 = np.array(lower_red)
    upper3 = np.array(upper_red)
    maskr = cv2.inRange(hsvf,lower3,upper3)
    resr = cv2.bitwise_and(frame, frame, mask =maskr)
    grayr = cv2.cvtColor(resr, cv2.COLOR_BGR2GRAY)
    ret, threshr = cv2.threshold(grayr,127,255,1)
    contoursr,h  = cv2.findContours(threshr,1,2)
    for cnt1 in contoursr :
        area = cv2.contourArea(cnt1)
        if area < 300000
            approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt1,True),True)
            if len(approx) == 4 :
                cv2.drawContours(frame,[cnt1],-1,(255,0,0),2)
                lower_mark = [cnt1[0]]
                xml = lower_mark[0][0][0]
                yml = lower_mark[0][0][1]
    lower4 = np.array(lower_blue)
    upper4 = np.array(upper_blue)
    maskb = cv2.inRange(hsvf, lower4,upper4)
    resb = cv2.bitwise_and(frame, frame, ,mask = maskb)
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
    tanb = (ymu - yml)/(float)(xmu - xml)
    tanr = (resource[r][0][1] - bsy)/(resource[r][0][0] - bsx)
    if (resource[r][0][0] - xmu) < 10 and (resource[r][0][1] - ymu) < 10:
        print "blink"
        f = 1;
    elif f == 0 :
        traverse()
    elif f == 1 :
        retrace()
    if xmu < bsx and ymu < bsy :
        f = 0
        r++;

cv2.imshow('brown',res1)
cv2.imshow('yellow',res)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
