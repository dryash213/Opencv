import cv2
#capturing image
# print('Import successfull')
#
# img=cv2.imread("Resources/friend.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)


#Cpturing and reading the video
# cap=cv2.VideoCapture("Resources/yoo.mp4")
# while True:
#     success, img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1)& 0xFF==ord('q'):
#         break

#Capture the webcam video
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break