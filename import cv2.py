import cv2
img = cv2.imread(r"C:\Users\USER\Desktop\hinh-nen-thien-nhien-phong-canh-dep-21_043147943.jpg")
gry =cv2.cvtColor(img,cv2.COLOR_BayerRG2GRAY)

sift = cv2.SIFT_create() 
sift = cv2.setContrastThreshold(0.3)
sift = cv2.setEgdeThreshold(5)

#detect key point and compute descpiptors
keypoint , desciptor = sift.detectAndCompute(gry,None)
for x in keypoint:
 print("({:.2f},{:.2f}) = size {:.2f) angle {:.2f}".format(x.pt[0], x.pt [1], x.size, x.angle))
kp = sift.detect (gry, None)
# Marking the keypoint on the image using circles
img = cv2.drawKeypoints (gry,
keypoint,
img,
flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT', img)
cv2.waitKey(0)
cv2.destroyAllWindows()