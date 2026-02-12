import cv2
 
# Load the image
image = cv2.imread("img.jpg")
 
# Define different scaling factors for width and height
fx = 0.1  
fy = 0.1  
 
# Apply different interpolation methods
resized_area = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
resized_linear = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
resized_nearest = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
 
# Display the resized images
cv2.imshow("Resized with INTER_AREA", resized_area)
cv2.imshow("Resized with INTER_LINEAR", resized_linear)
cv2.imshow("Resized with INTER_CUBIC", resized_cubic)
cv2.imshow("Resized with INTER_NEAREST", resized_nearest)
cv2.waitKey(0)
cv2.destroyAllWindows()