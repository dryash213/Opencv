import cv2
import numpy as np


img=cv2.imread("Resources/friend.jpg")
print(img.shape)

imgResize=cv2.resize(img,(623,480))


imgCroped=img[0:250,500:900]


cv2.imshow("Output0",imgCroped)
cv2.waitKey(0)
