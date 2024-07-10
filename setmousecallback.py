import cv2 
  
def drawcircle(event,x,y, flag, param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(rze,(x,y),10,(255,0,0),-1)

img = cv2.imread(r'C:\Users\USER\Pictures\Screenshots\Screenshot 2023-12-30 204446.png')
cv2.namedWindow("anh")
rze = cv2.resize(img,(600,590))

cv2.setMouseCallback("anh",drawcircle)

while(1):
    cv2.imshow("anh",rze)
   
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows 

# import cv2
# def drawCircle(event, x, y, flag, param):
#  if(event == cv2.EVENT_LBUTTONDOWN): 
#    cv2.circle(img, (x, y), 10, (255,0,0), -1)

# img = cv2.imread(r'C:\Users\USER\Pictures\Screenshots\Screenshot 2023-12-30 204446.png')
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', drawCircle)
# while(1):
#  cv2.imshow('image', img)
#  if cv2.waitKey(20) & 0xff == ord('q'):
#   break