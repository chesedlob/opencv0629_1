import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)

img[:, 0:133] = (255, 0, 0)     
img[:, 133:266] = (0, 255, 0)    
img[:, 266:400] = (0, 0, 255)    

blue = img[:, 0:133]
green = img[:, 133:266]
red = img[:, 266:400]


cv2.rectangle(blue, (30,100),(100,300),(255,255,255), 6)


cv2.circle(green, (66,200),50, (255,255,255), 6)

cv2.line(red, (30,100), (100,300), (255,255,255), 6)
cv2.line(red, (100,100), (30,300), (255,255,255), 6)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()