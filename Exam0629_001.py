import cv2 as cc
import numpy as np

image = np.ones((400,400),np.uint8)
image[:,:] = 255
title = "SquareX"
pt1 = (100,100)
pt2 = (300,300)
pt3 = (100,300)
pt4 = (300,100)
cc.rectangle(img=image,pt1=pt1,pt2=pt2,color=0,lineType=cc.LINE_4)
cc.line(image,pt3,pt4,color=0)
cc.line(image,pt2,pt1,color=0)
cc.imshow(title,image)


image2 = np.zeros((400,400,3),np.uint8)
image2[:,:,:] = 255
print(image2[:])
print("-------")
print(image2[:,:])
title2 = "SquareO"
pt1 = (100,100)
pt2 = (300,300)
center = (200,200)

cc.rectangle(image2,pt1,pt2,0,cc.LINE_4)
cc.circle(image2,center,100,0)
cc.imshow(title2,image2)
cc.waitKey(0)
cc.destroyAllWindows()
