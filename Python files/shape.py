import numpy as np
import cv2
i=1
a=[]
b=[]
cam=cv2.VideoCapture(1)
s,img1=cam.read()
#cv2.imshow("Test pic",img1)
#cv2.imwrite('2.bmp',img1)
img = cv2.imread('3.bmp')
img=cv2.GaussianBlur(img,(5,5),0)
gray = cv2.imread('3.bmp',0)
ret,thresh = cv2.threshold(gray,0,1,1)
contours,h = cv2.findContours(thresh,1,2)
l=len(contours)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
    print len(approx)
    if len(approx)==5 :
        print "pentagon"
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
        a=a+[cnt[0]]
    elif len(approx)==4 and i<=l-1:
        print "square"
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
        b=b+[cnt[0]]
    elif len(approx) == 9:
        print "half-circle"
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print "circle"
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)
    i=i+1
print "sqaures",b
print "traingle",a
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
