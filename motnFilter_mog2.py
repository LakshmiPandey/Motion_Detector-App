
####################################
#used to detect the moving object by removing the background
#here MOG2 mothod has been used

## this is much better and improved model for detect then MOG()
#####################################

import numpy as np
import cv2
cap = cv2.VideoCapture(0)

## this is for python 3.0 and plus version
foreground_background = cv2.createBackgroundSubtractorMOG2()

## for python version of 2.0 use the line given below
#  foreground_background = cv2.BackgroundSubtractorMOG2()



while True :
    ret, frame = cap.read()
    foreground_mask =  foreground_background.apply(frame)
    cv2.imshow("HERE_IS_THE_OUTPUT", foreground_mask)
    if cv2.waitKey(1) == 13 :   ## key 13 is for enter
        break

cap.release()
cv2.destroyAllWindows()
