import simulatorInterface
import cv2

def controller(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    cv2.imshow("car view", blur)
    cv2.waitKey(1)

    controlCommand={}
    controlCommand["speed"]=100
    controlCommand["steer"]=-0.5
    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()
