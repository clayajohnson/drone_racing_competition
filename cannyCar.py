import simulatorInterface
import cv2
import numpy as np
import math

def controller(image):
    # copy original image to display lanes on
    view = np.copy(image)
    # apply hsv filter to original image
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # blue and yellow copy for edge detection
    hsv_blue = hsv.copy()
    hsv_yellow = hsv.copy()
    # get blue and yellow maske from hsv
    blue_mask = cv2.inRange(hsv_blue,(100,120,165),(140,255,255))
    yellow_mask = cv2.inRange(hsv_yellow,(20,50,200),(60,255,255))
    # combine blue and yellow mask
    mask = cv2.bitwise_or(blue_mask,yellow_mask)
    # perform canny edge detection
    edges = cv2.Canny(mask,200,400)
    # define region of interest
    h,w = edges.shape
    roi_mask = np.zeros_like(edges)
    poly = np.array([[(0,0.5*h),(w,0.5*h),(w,h),(0,h)]],np.int32)
    cv2.fillPoly(roi_mask,poly,255)
    roi_edges = cv2.bitwise_and(edges,roi_mask)
    # detect line segments
    rho = 1
    angle = np.pi/180
    thresh = 10
    lines = cv2.HoughLinesP(roi_edges,rho,angle,thresh,np.array([]),minLineLength=8,maxLineGap=4)
    # combine line segments into lanes
    lanes = []
    left_lane = []
    right_lane = []
    left_bound = w*(1-1/3)
    right_bound = w*1/3
    if lines is not None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                if x1 == x2:
                    continue
                fit = np.polyfit((x1,x2),(y1,y2),1)
                slope = fit[0]
                intercept = fit[1]
                if slope < 0:
                    if x1 < left_bound and x2 < left_bound:
                        left_lane.append((slope,intercept))
                else:
                    if x1 > right_bound and x2 > right_bound:
                        right_lane.append((slope,intercept))
        left_lane_avg = np.average(left_lane,axis=0)
        right_lane_avg = np.average(right_lane,axis=0)
    if len(left_lane) > 0:
        lanes.append([[max(-w,min(2*w,int((h-left_lane_avg[1])/left_lane_avg[0]))),h,max(-w,min(2*w,int((h/2-left_lane_avg[1])/left_lane_avg[0]))),int(0.5*h)]])
    if len(right_lane) > 0:
        lanes.append([[max(-w,min(2*w,int((h-right_lane_avg[1])/right_lane_avg[0]))),h,max(-w,min(2*w,int((h/2-right_lane_avg[1])/right_lane_avg[0]))),int(0.5*h)]])
    # draw lanes over car view
    lane_image = np.zeros_like(view)
    if lanes is not None:
        for lane in lanes:
            for x1,y1,x2,y2 in lane:
                cv2.line(lane_image,(x1,y1),(x2,y2),(0,255,0),2)
    lane_view = cv2.addWeighted(view,0.8,lane_image,1,1)
    # calculate heading
    if len(lanes) < 2:
        heading = 0
    else:
        mid = int(0.5*w)
        if lanes[0] is None:
            x1,_,x2,_ = lanes[1][0]
            x_off = x1-x2
            y_off = int(0.5*h)
        elif lanes[1] is None:
            x1,_,x2,_ = lanes[0][0]
            x_off = x1-x2
            y_off = int(0.5*h)
        else:
            _,_,left_x2,_ = lanes[0][0]
            _,_,right_x2,_ = lanes[1][0]
            x_off = int((left_x2 + right_x2)/2 - mid)
            y_off = int(0.5*h)
        angle_to_heading = math.atan(x_off/y_off)
        heading = int(angle_to_heading*180/math.pi)*0.1
        if heading < -1:
            heading = -1
        elif heading > 1:
            heading = 1
    print(heading)
    # show view
    # cv2.imshow("lane view",lane_view)
    # cv2.waitKey(1)
    # steer according to heading
    controlCommand={}
    controlCommand["speed"]=3500
    controlCommand["steer"]=heading
    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()
