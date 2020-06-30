import simulatorInterface
import cv2
import numpy as np

def controller(image):
    # copy original image to display contours on
    view = np.copy(image)
    # apply hsv filter to original image
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # blue and yellow copy for edge detection
    hsv_blue = hsv.copy()
    hsv_yellow = hsv.copy()
    # get blue and yellow lines in hsv image
    blue_mask = cv2.inRange(hsv_blue,(100,120,165),(140,255,255))
    yellow_mask = cv2.inRange(hsv_yellow,(20,50,200),(60,255,255))
    # find contours (edges)
    blue_contours,hierarchy = cv2.findContours(blue_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    yellow_contours,hierarchy = cv2.findContours(yellow_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # # find the main blue contour
    # if blue_contours:
    #     main_blue_contour = None
    #     lowest_pt = 0
    #     for contour in blue_contours:
    #         if len(contour) < 50:
    #             continue
    #         this_lowest_index = np.argmax(contour[:,0,1])
    #         this_lowest_pt = contour[this_lowest_index,0,1]
    #         if this_lowest_pt > lowest_pt:
    #             lowest_pt = this_lowest_pt
    #             main_blue_contour = contour
    #     #cv2.circle(view,(main_blue_contour[lowest_pt][0][0],main_blue_contour[lowest_pt][0][1]),4,(255,0,255))
    # # find the main yellow contour
    # if yellow_contours:
    #     main_yellow_contour = None
    #     lowest_pt = 0
    #     for contour in yellow_contours:
    #         if len(contour) < 50:
    #             continue
    #         this_lowest_index = np.argmax(contour[:,0,1])
    #         this_lowest_pt = contour[this_lowest_index,0,1]
    #         if this_lowest_pt > lowest_pt:
    #             lowest_pt = this_lowest_pt
    #             main_yellow_contour = contour
    #     #cv2.circle(view,(main_yellow_contour[lowest_pt][0][0],main_yellow_contour[lowest_pt][0][1]),4,(255,0,255))
    # draw countours (green) on view
    cv2.drawContours(view,blue_contours,-1,(0,255,0),1)
    cv2.drawContours(view,yellow_contours,-1,(0,255,0),1)
    # redner detected edges
    cv2.imshow("detected edges",view)
    cv2.waitKey(1)

    controlCommand={}
    controlCommand["speed"]=100
    controlCommand["steer"]=0.5
    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()
