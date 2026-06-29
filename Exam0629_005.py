import cv2
import numpy as np


img = np.ones((500, 500, 3), dtype=np.uint8) * 255

cell = 100
row = 2
col = 2

while True:
    img[:] = 255

    for i in range(0, 501, cell):
        cv2.line(img, (i, 0), (i, 500), (0, 0, 0), 1)
        cv2.line(img, (0, i), (500, i), (0, 0, 0), 1)

    x1 = col * cell
    y1 = row * cell
    x2 = x1 + cell
    y2 = y1 + cell

    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), -1)

    cv2.imshow("src", img)

    key = cv2.waitKeyEx(0)

    if key == ord('q'):
        break


    elif  key == 0x250000:
        if col > 0:
            col -= 1


    elif key == 0x260000:
        if row > 0:
            row -= 1


    elif key == 0x270000:
        if col < 4:
            col += 1

    elif  key == 0x280000:
        if row < 4:
            row += 1

cv2.destroyAllWindows()