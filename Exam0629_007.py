import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype=np.uint8) * 255

drawing = False
old_x, old_y = -1, -1

def nothing(x):
    pass

def mouse(event, x, y, flags, param):
    global drawing, old_x, old_y

    color_num = cv2.getTrackbarPos("Color", "img")

    if color_num == 0:
        color = (255, 0, 0)      
    elif color_num == 1:
        color = (0, 255, 0)     
    else:
        color = (0, 0, 255)     
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        old_x = x
        old_y = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (old_x, old_y), (x, y), color, 2)
            old_x = x
            old_y = y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


cv2.namedWindow("img")
cv2.createTrackbar("Color", "img", 0, 2, nothing)
cv2.setMouseCallback("img", mouse)

while True:
    cv2.imshow("img", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()