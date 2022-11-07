import  cv2

image = cv2.imread("images/1578955240cm_vector.png")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshImage =  cv2.threshold(grayImage, 90, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite("images/Threshold image1.png",threshImage) #good image

cv2.imshow("Thresh ",threshImage) #show original image
cv2.imshow("Grey Image ",grayImage) #show grey image
#threshImage =  cv2.threshold(grayImage, 200, 255, cv2.THRESH_BINARY)[1]

#cv2.imwrite("Threshold image.png",threshImage) #bad image
cv2.waitKey(0) # wait for no seconds and display continually

cv2.destroyAllWindows() #close