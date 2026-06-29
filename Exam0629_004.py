import cv2 as cc
import numpy as np


image = np.zeros((300,300),np.uint8)
title = ""

cc.putText(image,f"{0}",(100,100), cc.FONT_HERSHEY_COMPLEX,3,255,3)
cc.imshow(title,image)
def Timer():
    i = 0   
    while True:
        ke = cc.waitKey(1000)
        if ke == ord('r'):
            i = 0
        if ke == ord('q'):
            break
        cc.putText(image,f"{i}",(100,100), cc.FONT_HERSHEY_COMPLEX,3,255,3)
        i +=1
        cc.imshow(title,image)
        image[:,:] = 0

if cc.waitKey(0) == ord('s'):
    Timer()
cc.destroyAllWindows()
       
