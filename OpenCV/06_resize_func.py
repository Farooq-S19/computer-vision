import sys
import cv2 as cv
src=cv.imread('image/lamp.jpg')
def resizeFrames(src,scale=0.01):
    height=int(src.shape[0]*scale)
    width=int(src.shape[1]*scale)
    resized=cv.resize(src,(width,height),interpolation=cv.INTER_AREA)
    return resized
resized=resizeFrames(src,0.99)
cv.imshow("img",resized)
cv.imshow("img_!",src)
cv.imwrite('lamp_1.jpg',resized)
if 0xFF==ord('q'):
    sys.exit('completed')

cv.waitKey(0)