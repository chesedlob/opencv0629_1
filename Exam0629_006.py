import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype=np.uint8) * 255

x = 250
y = 250

cv2.imshow("img", img)

while True:
    key = cv2.waitKeyEx(0)

    if key == ord('q'):
        break

    old_x = x
    old_y = y

    if key == 81 or key == 0x250000:
        x = max(0, x - 50)


    elif key == 82 or key == 0x260000:
        y = max(0, y - 50)

    elif key == 83 or key == 0x270000:
        x = min(500, x + 50)

    elif key == 84 or key == 0x280000:
        y = min(500, y + 50)

    cv2.line(img, (old_x, old_y), (x, y), (255, 0, 0), 3)

    cv2.imshow("img", img)

cv2.destroyAllWindows()