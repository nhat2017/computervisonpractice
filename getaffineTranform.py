import cv2 
import numpy as np

img = cv2.imread(r'C:\Users\USER\Pictures\Screenshots\Screenshot 2024-01-02 114540.png')
rze = cv2.resize(img,(0,0),fx=0.25,fy=0.25)
cot,hang = rze.shape[0:2]

input = np.float32([[0,0],[0,cot-1],[hang-1,0]])
output =np.float32([[0,0],[cot/2,0],[cot/2,hang/2]])
M = cv2.getAffineTransform(input,output)
dst =cv2.warpAffine(rze,M,[cot,hang])

img1 =cv2.hconcat(rze,dst)
cv2.imshow("anh",img1)
cv2.waitKey(0) & 0xff == ord('q')


