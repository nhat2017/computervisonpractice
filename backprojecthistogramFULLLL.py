import numpy as np
import cv2 as cv
 
roi = cv.imread(r'C:\Users\USER\Pictures\Saved Pictures\world-cup-bounou-becomes-first-african-goalkeeper-with-three-clean-sheets-800x450.jpeg')

hsv = cv.cvtColor(roi,cv.COLOR_BGR2HSV)
 
target = cv.imread(r'C:\Users\USER\Pictures\Saved Pictures\copy.jpeg')

hsvt = cv.cvtColor(target,cv.COLOR_BGR2HSV)
 
# calculating object histogram
roihist = cv.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
 
# normalize histogram and apply backprojection
cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
dst = cv.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
 
# Now convolute with circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(dst,-1,disc,dst)
 
# threshold and binary AND
ret,thresh = cv.threshold(dst,50,255,0)
thresh = cv.merge((thresh,thresh,thresh))
res = cv.bitwise_and(target,thresh)
 
res = np.vstack((target,thresh,res))
#cv.imwrite('res.jpg',res)
cv.imshow("anh",dst)
cv.imshow("anh1",res)

cv.waitKey(0) & 0xff == ord('q')