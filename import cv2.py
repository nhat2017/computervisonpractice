import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\USER\Downloads\81700f13-a3c8-4523-8347-b6371cb6bec5.jpg")
img2 =cv2.imread(r"C:\Users\USER\Downloads\download.jpg")

sift =cv2.SIFT_create()
sift.setContrastThreshold(0.03)
sift.setEdgeThreshold (5)

#Detect key points and compute descriptors
keypoints, descriptors = sift.detectAndCompute (img1, None)
keypoints2, descriptors2 = sift.detectAndCompute (img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
matches = bf.match(descriptors,descriptors2)
matches = sorted(matches, key = lambda x:x.distance)
img3 = cv2.drawMatches(img1, keypoints ,img2, keypoints2, matches[:50], img2, flags=2)
matches = bf.knnMatch (descriptors, descriptors2, k = 2)
good = []
for m,n in matches:
 if m.distance < 0.8*n.distance:
  good.append([m])

  
img4 = cv2.drawMatchesKnn(img1,keypoints,img2, keypoints2,good, None,
matchColor=(0, 255, 0), matchesMask=None,
singlePointColor=(255, 0, 0), flags=0)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50) # or pass empty dictionary
flann = cv2.FlannBasedMatcher (index_params, search_params)
flann = cv2.FlannBasedMatcher (index_params, search_params)
matches = flann.knnMatch(descriptors, descriptors2, k=2)
# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]
# ratio test as per Lowe's paper
for i, (m,n) in enumerate (matches):
  if m.distance < 0.8*n.distance:
   matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),
singlePointColor = (255,0,0),
matchesMask = matchesMask,
flags = cv2.DrawMatchesFlags_DEFAULT)

img5 = cv2.drawMatchesKnn(img1, keypoints, img2, keypoints2, matches, None, **draw_params) 
img6 = cv2.resize(img5,[800,400])


cv2.imshow('SIFT', img6)
cv2.waitKey(0)
cv2.destroyAllWindows()
