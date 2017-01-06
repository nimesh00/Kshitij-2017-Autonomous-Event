import cv2
import numpy as np
import serial

ser=serial.Serial('')

cap=cv2.VideoCapture(0)

ly=[20,100,30]
uy=[40,255,255]

lb=[9,95,95]
ub=[17,255,255]

lp=[125,120,30]
up=[255,255,255]

lbl=[100,150,0]
ubl=[120,255,255]

a=[[[1,0]]]
b=[[[0,0]]]

p=[[[1,0]]]
bl=[[[0,1]]]
cx=[1]
cy=[0]
px=[0]
py=[0]

c=[]

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame=cv2.GaussianBlur(frame,(9,9),0)
    lowery=np.array(ly)
    uppery=np.array(uy)
    mask=cv2.inRange(hsv,lowery,uppery)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,1)
    contours,h=cv2.findContours(thresh,1,2)
    for cnt in contours:
        if cv2.contourArea(cnt) > 10 and cv2.contourArea(cnt) < 30000:
            approx=cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
            if len(approx)== 4 or len(approx)==3:
                c=c+[cnt[0]]
                cv2.drawContours(frame,[cnt],-1,(255,0,0))
               
    lower_blue=np.array(lb)
    upper_blue=np.array(ub)
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,1)
    contours,h=cv2.findContours(thresh,1,2)
    for cnt1 in contours:
        if cv2.contourArea(cnt1) > 10 and cv2.contourArea(cnt1) < 30000:
            approx=cv2.approxPolyDP(cnt1,0.1*cv2.arcLength(cnt1,True),True)
            if len(approx)== 4:
                b=[cnt1[0]]
                cv2.drawContours(frame,[cnt],-1,(0,255,0))

    lowery=np.array(lp)
    uppery=np.array(up)
    mask=cv2.inRange(hsv,lowery,uppery)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,1)
    contours,h=cv2.findContours(thresh,1,2)
    for cnt in contours:
        if cv2.contourArea(cnt) > 10 and cv2.contourArea(cnt) < 30000:
            approx=cv2.approxPolyDP(cnt,0.03*cv2.arcLength(cnt,True),True)
            if len(approx)== 4:
                M=cv2.moments(cnt)
                x=int(M['m10']/M['m00'])
                y=int(M['m01']/M['m00'])
                cx=cx+[x]
                cy=cy+[y]
                
               
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
                px=px+[g]
                py=py+[f]
                

    for i in range(8):
        a=a+[c[i]]
    # COORDINATES
    #x1,y1 - for townhall
    #x2,y2 - for resource
    #x11,y11 - for pink marker
    #x21,y21 - for blue marker
    
    #TOWNHALL AND RESOURCE
    x1=a[-1][0][0]
    y1=a[-1][0][1]

    for i in range (len(b)-1):    
        x2= b[i+1][0][0]
        y2=b[i+1][0][1]

        pt=(x1,y1)
        q=(x2,y2)
        cv2.line(frame,pt,q,(0,255,0))
        
        #slope for resource and townhall
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

        while(a1 != a2 ):
            ser.write('r')#rotate
        if(a1==a2):
            for j in range (2):
                while((x21 not in x2 )and (y21 not in y2)):
                    ser.write('f')#forward
                if((x21 in x2) and (y21 in y2)):
                    ser.write('l')#led
                while((x11 not in x1) and (y11 not in y1)):
                    ser.write('b')
                if((x11 in x1) and (y11 in y1)):
                    ser.write('l')
        
    cv2.imshow('res',frame)
    k=cv2.waitKey(5) & 0xFF
    if(k==27):
        break
cap.release()
cv2.destroyAllWindows()
