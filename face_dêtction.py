import cv2
import numpy as np

# Load the image
img1 = cv2.imread(r'C:\Users\USER\Pictures\Camera Roll\WIN_20240412_09_54_25_Pro.jpg', cv2.IMREAD_GRAYSCALE)  # Use a face template image
img1 = cv2.resize(img1, (400, 600))  # Resize to match the webcam frame size

# Applying the SIFT detector
sift = cv2.SIFT_create()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces

# Detect key points and compute descriptor for the template image
keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

cap = cv2.VideoCapture(0)  # Start video capture

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.resize(frame, (500, 700))  # Resize to match the template image size
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # Detect key points and compute descriptor for the frame
    keypoints_2, descriptors_2 = sift.detectAndCompute(gray, None)

    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Apply ratio test
    good_matches = []
    for (x, y, w, h) in faces:
    # Extract the facial ROI
     face = gray[y:y+h, x:x+w]

    # Find contours in the facial ROI
     _, contours, _ = cv2.findContours(face, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours (optional)
     if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)

        # Draw the contour around the face
        cv2.drawContours(img, [largest_contour], -1, (0, 255, 0), 2)

cap.release()
cv2.destroyAllWindows