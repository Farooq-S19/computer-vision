import cv2 as cv
img_1=cv.imread("img.jpg")
x=img_1.shape[0]//8
y=img_1.shape[1]//8
img = cv.resize(img_1,(y,x),fx=None,fy=None,interpolation=cv.INTER_AREA)
# Gray
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Blur
img_blur = cv.GaussianBlur(img,(7,7),cv.BORDER_CONSTANT)
# Canny edge detection
img_canny = cv.Canny(img,150,300)
#dilute 
dilute = cv.dilate(img_canny,(5,5),iterations=3)
eroded = cv.erode(dilute,(5,5),iterations=3)
cv.imshow("resized ",img)
# cv.imshow("gray img", img_gray)
# cv.imshow('Blur', img_blur)
# cv.imshow("canny edge detection",img_canny)
cv.imshow('Dilated',dilute)
cv.imshow('Eroded',eroded) 
#cropping the image
cropped = img[50:240,10:150]
cv.imshow("cropped image",cropped)
cv.waitKey(0)