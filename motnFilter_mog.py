
####################################
#used to detect the moving object by removing the background
#here MOG mothod has been used
#####################################


import cv2
import numpy as np

cap =  cv2.VideoCapture(0)

## this is for python 3.0 and plus version
foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG()

## for python version of 2.0 use the line given below
##  foreground_background = cv2.createBackgroundSubtractorMOG()


while True:
    ret, frame = cap.read()

    foreground_mask  = foreground_background.apply(frame)

    cv2.imshow("OUTPUT", foreground_mask)
    if cv2.waitKey(1) == 32 :  ## key 32  is tab
        break

cap.release()
cv2.destroyAllWindows()
