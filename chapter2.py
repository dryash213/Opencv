import cv2
import numpy as np


img=cv2.imread("Resources/friend.jpg")

kernel=np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ingBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(img,100,200)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
# cv2.imshow("Output0",imgGray)
# cv2.imshow("Output0",imgDialation)
cv2.imshow("Output0",imgEroded)
# cv2.imshow("Output1",imgCanny)
# cv2.imshow("Output2",ingBlur)
cv2.waitKey(0)
