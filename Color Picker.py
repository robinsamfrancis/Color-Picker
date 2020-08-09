import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def empty(a):
    pass
#path= "Resources/Lambo.jpg"



#Creating Taskbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,480) #Creating trackbar size
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",146,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Value Min","TrackBars",169,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

#Reading the taskbars

while True: #inorder to get the value we have to put it in a loop, otherwise we have to run the code again and again
    _,img= cap.read()
    imghsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min= cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")

    #Creating a mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imghsv, lower, upper)
    imgResult= cv2.bitwise_and(img,img,mask= mask )





    cv2.imshow("HSV", imghsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2. waitKey(1)


