import array
import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3))
#white rectangle
rect=cv.rectangle(blank,(150,150),(350,350),(200,200,200),-1)
#yellow border
rect=cv.rectangle(blank,(151,151),(351,351),(10,00,00),2)
#diagonal using line
lines= cv.line(rect,(150,150),(350,350),(5,0,10),1)
line2=cv.line(rect,(350,150),(150,350),(5,0,10),1)
#a circle inside the sqaure
circles = cv.circle(lines,(250,250),100,(0,0,0),1)
circles = cv.circle(lines,(250,250),45,(0,0,0),1)
ellipse = cv.ellipse(circles,(250,250),(100,50),45,0,360,(250,0,0),1)
ellipse = cv.ellipse(circles,(250,250),(96,46),45,0,360,(250,0,0),1)
ellipse = cv.ellipse(circles,(250,250),(45,22),135,0,360,(250,0,0),1)
ellipse = cv.ellipse(circles,(250,250),(96,46),135,0,360,(0,0,255),1)
ellipse = cv.ellipse(circles,(250,250),(45,22),45,0,360,(0,0,255),1)
ellipse = cv.ellipse(circles,(250,250),(100,50),135,0,360,(0,0,255),1)
text = cv.putText(blank,"Diagram",(200,370),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(0,200,0),1)
# cv.imshow("diagram",circle)
cv.imshow("line",lines)
# cv.imshow("rectangle",rect)
cv.waitKey(0)
cv.destroyAllWindows()