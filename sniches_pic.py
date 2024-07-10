import cv2
import pandas
import numpy as np
import matplotlib.pyplot as plt

def feauture_matching(img1 , img2,ratio = 0.75 ,  show = False):
    sift = cv2.SIFT.create()
    sift.setContrastThreshold(0.03)
    sift.setEdgeThreshold(5)
    
    kp1,des1 = sift.detectAndCompute(img1,None)
    kp2,des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm= FLANN_INDEX_KDTREE, trees = 5)
    search_params =dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des2,des1,k=2)
    matchesMaskRatio =[(0,0) for i in range(len(matches))]
    matchDict = []
    for i , (m,n) in enumerate(matches):    
        if m.distance <ratio*n.distance:
            matchesMaskRatio[i] = [1,0]
            matchDict[m.trainIdx] = m.queryIdx
           
    good = []
    recipMatches = flann.knnMatch(des1,des2,k=2)
    matchesMaskRatioRecip = [(0,0) for i  in range(len(recipMatches))]
   
    for i,(m,n) in enumerate(recipMatches):
        if m.distance <ratio*n.distance:
            if m.queryIdx in matchDict  and matchDict[m.queryIdx] == m.trainIdx:
                good.append(m)
                matchesMaskRatioRecip[i] =[1,0]
    if show:
        drawParams = dict(matchColor = (0,255,0),singlePointColor=(255,0,0), matchesMask = matchesMaskRatioRecip,flags =0)
       
       
        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,recipMatches,None,**drawParams)
        plt.figure(),plt.xticks([]),plt.yticks([])
        plt.imshow(img3,)
    return ([kp1[m.queryIdx].pt for m  in good], [kp2[m.trainIdx].pt for m in good])
def getMatrixTransform(src,dst,method ='homography'):
    pts1,pts2 = feauture_matching(src,dst)
    srcPts =np.float32(pts1).reshape(-1,1,2)
    dstPts =np.float(pts2).reshape(-1,1,2)
    if method ==' affine':
        H, mask =cv2.estimateAffine2D(srcPts,dstPts,cv2.RANSAC,ransacReprojThreshold=5.0)
    matchMask = mask.ravel().tolist()
    return (H,pts1,pts2, mask)
def Perspective_warping(img1,img2,img3):
    img1_padded = cv2.copyMakeBorder(img1, top= 50, bottom = 50 , left = 50,right=500, borderType= cv2.BORDER_CONSTANT)
    (M1,pts1,pts2,_) =  getMatrixTransform(img2,img1_padded,method="hemography")
    (M2,_,_,_) = getMatrixTransform(img3,img1_padded, method="homography")
    out1 = cv2.warpPerspective(img2,M1 ,(img1_padded.shape[1],img1_padded.shape[0]))
    out2 = cv2.warpPerspective(img3,M2 ,(img1_padded.shape[1],img1_padded.shape[0]))

    mask1= np.zeros_like(img1_padded,dtype =np.float32)
    mask2 = np.zeros_like(img1_padded,dtype=np.float32)
    cv2.fillPoly(mask1, pts=[np.int32(pts1)],color=(1,1,1))
    cv2.fillPoly(mask2, pts=[np.int32(pts1)],color=(1,1,1))
    
img1 =cv2.imread(r'C:\Users\USER\Pictures\Saved Pictures\img1oke.png')
img2 = cv2.imread(r"C:\Users\USER\Pictures\Saved Pictures\img2oke.png")
img3= cv2.imread(r"C:\Users\USER\Pictures\Saved Pictures\img3oke.png")
Perspective_warping(img1,img2,img3)



