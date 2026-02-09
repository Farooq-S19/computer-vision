import cv2 as cv
import sys

capture = cv.VideoCapture('leaves.mp4')
while True:
    isTrue, frames =capture.read()
    cv.imshow('frames',frames)
    if cv.waitKey(40) & 0xFF ==ord('q'):
        sys.exit("completed")
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
