import imutils
import cv2

#redLower = (27, 47, 150)
#redUpper = (179, 255, 255)

#color code of my object
redLower = (15, 164, 162) 
redUpper = (45, 232, 255)

camera = cv2.VideoCapture(1)

while True:
    #read the frames from the camera
    (grabbed,frame) = camera.read()

    frame = imutils.resize(frame, width = 600) #resize the frame
    blurred = cv2.GaussianBlur(frame, (11, 11), 0) #smoothening the blur
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #convert the image from BGR/RGB to HSV

    mask = cv2.inRange(hsv,redLower, redUpper) #mask the green color to
    mask = cv2.erode(mask, None, iterations=2) #erosion the mask with leftovers
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2] #find the contours

    center = None

    if len(cnts) > 0:
        c = max(cnts, key = cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c) #needs a midpoint and diameter
        M = cv2.moments(c)
        center = (int (M["m10"] / M["m00"] ), int (M["m01"] /   M["m00"]))

        if radius > 10:
            #two circles are drawn
            cv2.circle(frame, (int (x), int (y)), int (radius), (0, 255, 255), 2) 
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            #print (center,radius)
            if radius > 250:
                print("stop")
            else:
                if(center[0] < 150):
                    print("Left")
                elif(center[0] > 450):
                    print("Right")
                elif(radius < 250):
                    print("Front")
                else:
                    print("Stop")

    cv2.imshow("Frame", frame) #show
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

