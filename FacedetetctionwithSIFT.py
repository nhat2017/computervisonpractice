import cv2 
import numpy as np
img1 = cv2.imread(r"C:\Users\USER\Pictures\Camera Roll\WIN_20240405_09_16_18_Pro.jpg")

sift = cv2.SIFT_create()

sift.setContrastThreshold(0.03)
sift.setEdgeThreshold(5)

keypoint, descriptor = sift.detectAndCompute(img1, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher (index_params, search_params)

cap =cv2.VideoCapture(0)
while True:
    ret, frame =cap.read()
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    keypoint2, descriptor2 = sift.detectAndCompute (gray, None)
    bf = cv2.BFMatcher()
    matches = flann.knnMatch (descriptor, descriptor2, k=2)
    good = []
    for m, n in matches:
     if m.distance <= 0.9 * n.distance: good.append([m])
   
    img3 = cv2.drawMatchesKnn (img1, keypoint, gray, keypoint2, good, None, matchColor=(0, 255, 0), matchesMask=None, singlePointColor=(255, 0, 0), flags=0)
    cv2.imshow('Flann Match', img3)
    if len (good) >= 10:
     src_pts = np.float32([keypoint[m[0].queryIdx].pt for m in good]).reshape(-1, 1, 2)
     dst_pts = np.float32([keypoint2[m[0].trainIdx].pt for m in good]).reshape(-1, 1, 2)

