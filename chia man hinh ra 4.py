import cv2
import numpy as np  
cap = cv2.VideoCapture(0)
anh1 = cv2.imread(r'C:\Users\USER\Pictures\Screenshots\Screenshot 2023-12-12 140017.png')

anh2 = cv2.resize(anh1,(240,320))

while True:
    ret, frame = cap.read()
    img = np.zeros(frame.shape,np.uint8)

    rze = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.putText(img,"Đẹp trai hông thầy",[50,50],fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale = 10, color =[255,122,234])
    height = int(cap.get(4))
    ret,haha = cv2.threshold(rze,120,250,cv2.THRESH_BINARY)
    width = int(cap.get(3))
    img[:height//2,:width//2] = cv2.rotate(rze,cv2.ROTATE_180)
    img[:height//2,width//2:] = rze

    img[height//2:,:width//2] = cv2.rotate(rze,cv2.ROTATE_180)
    img[height//2:,width//2:] = haha
   


    cv2.imshow("anh chia doi",img)
    
    if cv2.waitKey(2) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()




















# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0)
 
# def drawcircle(event,x,y,flag, param):
#    if(event == cv2.EVENT_LBUTTONDOWN):
#      # Access the global variable 'circles' to store circle coordinates
#          global circles        
#          circle.append((x, y))  # Add clicked coordinates to the list

 
# cv2.namedWindow('anh')
# cv2.setMouseCallback('anh',drawcircle)

# circle = []
# while True:
#     ngang= int(cap.get(3)) #lay chieu rong
#     doc = int(cap.get(4)) # lay chieu dai
#     ret,frame = cap.read()
#     img = np.zeros(frame.shape,np.uint8)
#     np.zeros()
#     cv2.circle(img,(200,150),10,(253,12,24),-1)
#     if circle:
#         for (x, y) in circle:
#             cv2.circle(img, (x, y), 10, (255, 0, 0), -1)


    
#     small = cv2.resize(frame,(0,0),fx = 0.5, fy= 0.5)
#     img[:doc//2,:ngang//2 ] = cv2.rotate(small,cv2.ROTATE_180)
#     img[doc//2:,:ngang//2] =small
#     img[:doc//2,ngang//2:] = cv2.rotate(small,cv2.ROTATE_180)
#     img[doc//2:,ngang//2:] = small
#     cv2.imshow("anh",img)
#     if cv2.waitKey(15) & 0xFF == ord('q'):
#      break


# cv2.destroyAllWindows

# import cv2
# import numpy as np

# def draw_circle(event, x, y, flags, param):
#     # Check if left mouse button is pressed down
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Access the global variable 'circles' to store circle coordinates
#         global circles
#         circles.append((x, y))  # Add clicked coordinates to the list

# # Initialize an empty list to store circle coordinates
# circles = []


# cap = cv2.VideoCapture(0)



# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cv2.namedWindow('Video with Circles')

# cv2.setMouseCallback('Video with Circles', draw_circle)

# while True:
#     ret, frame = cap.read()

#     if circles:
#         for (x, y) in circles:
#             cv2.circle(frame, (x, y), 10, (255, 123, 214), -1)

#     # Display the frame with circles
#     cv2.imshow('Video with Circles', frame)

#     # Exit loop on 'q' key press or window close event
#     if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty('Video with Circles', cv2.WND_PROP_VISIBLE) < 1:
#         break

# # Release the video capture object
# cap.release()

# # Close all open windows
# cv2.destroyAllWindows()
