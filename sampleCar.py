def controller(image):
    #cv2.imshow("car view",image)
    #cv2.waitKey(1)


    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #ret,thresh = cv2.threshold(hsv_image,127,100,0)
    #contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #print(len(contours))
    upper_blue = np.array([500,300,400])
    #lower_blue = np.array([150,150,20])
    lower_blue = np.array([50,50,0])
    #ret,thresh = cv2.threshold(hs)

    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    #_,contour,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(image,contour,-1,(0,255,0),3)

    res = cv2.bitwise_and(image,image,mask=mask)
    h, w, _ = image.shape
    flag = False
    x = 0
    y = 0
    controlCommand={}
    #controlCommand["steer"]= 5
    #controlCommand["speed"]=10

    #print(res)



    for i in range(0,h):
        for j in range(0,w):
            if res[i][j][2] >0:
                x = i
                y = j
                flag = True
                break
        if flag == True:
            break

    z = math.sqrt(((240 - h)**2) + ((320 - y)**2))
    print(z)

    if z <= 200:
        controlCommand["steer"]= 5
        controlCommand["speed"]=1000
    else:
        controlCommand["steer"]= 100
        controlCommand["speed"]=1000


    #else:
    #    controlCommand["steer"]= 0






    cv2.imshow("car view",res)
    cv2.waitKey(1)






    #(b,g,r)=cv2.split(image)
    #if b[0][0] > 200:
    #    controlCommand["speed"]=100
    #    controlCommand["steer"]= 0
    #print(b)



    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()
