import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

for i in range(10):
   _,frame =cap.read()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

last = gray



while True:

    _ , frame =cap.read()
#cvt frame ve gray ne 
    gray1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  # dung hang absdiff tru di frame goc
    abs =cv2.absdiff(last,gray1)
    last = gray1
    ret ,anh = cv2.threshold(abs,30,255,cv2.THRESH_BINARY)
    # tim duong vien vat the
    coutours , _ = cv2.findContours(anh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  
    # ham for de loai bo vat the nho á nè 
    for countour in coutours:
        if cv2.contourArea(countour) > 600:
            
        
         x,y,w,h =cv2.boundingRect(countour) #chon cai hinh chu nhat xat nut nhat 
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 


   
    cv2.imshow("anh" , frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()