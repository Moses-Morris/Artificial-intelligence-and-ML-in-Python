import cv2 as cv

video = cv.VideoCapture() # initialize camera

while True:
    _,img = video.read() #read the frame from the camera
    #read function takes 2 parameters

    cv.imshow("VideoStream", img) #show the frame if in live stream

    key = cv.waitKey(1) & 0xFF   #record the keypress

    if key == ord("q"):  # if the key pressed is q break the while loop
        video.release()  # release the camera

    cv.destroyAllWindows() #every opened output will be closed