import cv2 as cv
from matplotlib import units
import numpy as np
blank = np.zeros((500,500,3))
blank_2 = np.zeros((500,500,3))
colored = np.full((500,500,3),[150,10,100] ,dtype=np.uint8)
blank[200:300]=255,0,0
cv.imshow("Black", blank)
blank_2[200:300,200:300]=255,45,0
cv.imshow("Black_2", blank_2)
cv.imshow("Colored", colored)
# cv.imshow("Black", blank_color)
cv.waitKey(0)
cv.destroyAllWindows()