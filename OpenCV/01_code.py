import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

img_path ='C:/Users/shaik/Desktop/IIITDM/OpenCV/img.jpg'
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(12,5))
plt.subplot(1,4,1)
plt.imshow(img)
plt.title("Original Image(BGR)")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(img_rgb)
plt.title("Original Image(RGB)")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(img_gray)
plt.title("Original Image(GRAY)")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(img_hsv)
plt.title("Original Image(HSV)")
plt.axis("off")
plt.show()