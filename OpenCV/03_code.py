import cv2 as cv 
import sys

img = cv.imread(cv.samples.findFile('IMG_20251210_180430.jpg'))
cv.imshow("img",img)
cv.waitKey(0)