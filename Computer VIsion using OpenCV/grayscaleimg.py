import cv2 #library  import opencv
img = cv2.imread("images/1578955240cm_vector.png")   #read the image

grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert  to gray

cv2.imwrite("images/grayImage.jpg",grayImage)  #save the image to new title after editing


cv2.imshow("Original ",img) #show original image
cv2.imshow("Grey Image ",grayImage) #show grey image

cv2.waitKey(0) # wait for no seconds and display continually

cv2.destroyAllWindows() #close