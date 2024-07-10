import cv2 as cv
import numpy as np
 
cap = cv.VideoCapture(0)
 
while(1):
 
    
    _, frame = cap.read()
 
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    
    lower_blue = np.array([70,50,50])
    upper_blue = np.array([180,255,255])
 
     # chọn range của ảnh
    mask = cv.inRange(hsv, lower_blue, upper_blue)
 
    # cộng ảnh frame 
    res = cv.bitwise_and(frame,frame, mask= mask)
    # khoanh vung anh trong cai mask 
    countours, hierachy = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    for pic , countour in enumerate(countours):
        #chi lay nhung coutours to 
        if cv.contourArea (countour)> 300:
           x,y,w,h =  cv.boundingRect(countour)
           vehinh = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3) 

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv.destroyAllWindows()