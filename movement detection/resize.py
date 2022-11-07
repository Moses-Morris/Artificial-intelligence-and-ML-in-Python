import cv2 as cv
import imutils
img = cv.imread("../Computer VIsion using OpenCV/images/Vivacious.jpg")

resizeImg = imutils.resize(img, width = 500)

cv.imwrite("Vivacious22.jpg", resizeImg)


