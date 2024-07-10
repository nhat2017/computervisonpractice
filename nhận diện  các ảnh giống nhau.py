import cv2
s_img = cv2.imread(r'C:\Users\USER\Pictures\Saved Pictures\world-cup-bounou-becomes-first-african-goalkeeper-with-three-clean-sheets-800x450.jpeg')
s_img = cv2.cvtColor(s_img, cv2.COLOR_BGR2RGB) #chuyển kênh màu
t_img = cv2.imread(r'C:\Users\USER\Pictures\Saved Pictures\copy.jpeg')
t_img = cv2.cvtColor(t_img, cv2.COLOR_BGR2RGB) #chuyển kênh  màu
method = eval('cv2.TM_CCOEFF')
s_img_copy = s_img.copy()
#HÀM dùng để  đối chiếu các vùng giống nhau
res = cv2.matchTemplate(s_img_copy, t_img, method)

#Xac dinh va ve vung nhan dang
min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(res) 

if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
  top_left = min_loc
else:
  top_left = max_loc

heigh, width, channel = t_img.shape

bottom_right = (top_left[0]+width, top_left[1]+heigh) 

cv2.rectangle(s_img, top_left, bottom_right, (255, 0, 0), 1)
#Hien thi 2 buc anh
cv2.imshow("anh ket qua", s_img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
 cv2.destroyAllWindows()