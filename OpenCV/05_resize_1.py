import cv2 as cv
import numpy as np
img=cv.imread('img.jpg')
height=img.shape[0]
width= img.shape[1]
width_resize=400
ratio=width_resize/width
height_resize=int(height*ratio)
resized_img=cv.resize(img,(width_resize,height_resize), interpolation=cv.INTER_AREA)
cv.imshow("resize",resized_img)
cv.waitKey(0)