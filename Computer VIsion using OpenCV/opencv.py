import cv2 #library  import opencv
img = cv2.imread("images/Vivacious.jpg")   #read the image
cv2.imwrite("images/Vivacious2.jpg", img)   #save the image

cv2.imshow("python", img) #show the image

cv2.waitKey(0)

cv2.destroyAllWindows() 