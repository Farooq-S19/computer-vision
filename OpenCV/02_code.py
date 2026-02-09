import cv2 as cv
img = cv.imread('C:/Users/shaik/Desktop/IIITDM/openCV/img.jpg')
img_re = cv.resize(img,(500,300))
cv.imshow('img',img)
cv.imshow('resized',img_re)
cv.imwrite('resized.jpg',img_re)
cv.waitKey(0)
