import simulatorInterface
import cv2
import numpy as np

def controller(image):
    imcopy = np.copy(image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_mask = cv2.inRange(hsv,(100,60,100),(115,255,255))
    contours,hierarchy = cv2.findContours(hsv_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(imcopy,contours,-1,(0,255,0),1)
    cv2.imshow("result",imcopy)
    cv2.waitKey(1)

    controlCommand={}
    controlCommand["speed"]=100
    controlCommand["steer"]=0
    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()
