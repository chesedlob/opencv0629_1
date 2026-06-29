import cv2 as cc
import numpy as np

image = cc.imread("lenna.bmp",cc.IMREAD_COLOR)
ver_pt1 = (512//4,0)
ver_pt2 = (512//4,512)

ver_pt3 = ((512//4) *2,0)
ver_pt4 = ((512//4) *2,512)

ver_pt5 = ((512//4) *3,0)
ver_pt6 = ((512//4) *3,512)

ho_pt1 = (0,512//4,)
ho_pt2 = (512,512//4)

ho_pt3 = (0,(512//4) *2)
ho_pt4 = (512,(512//4) *2)

ho_pt5 = (0,(512//4) *3)
ho_pt6 = (512,(512//4) *3)

cc.line(image,ver_pt1,ver_pt2,(255,255,255))
cc.line(image,ver_pt3,ver_pt4,(255,255,255))
cc.line(image,ver_pt5,ver_pt6,(255,255,255))

cc.line(image,ho_pt1,ho_pt2,(255,255,255))
cc.line(image,ho_pt3,ho_pt4,(255,255,255))
cc.line(image,ho_pt5,ho_pt6,(255,255,255))
title = "Exam002"
cc.imshow(title,image)
cc.waitKey(0)
cc.destroyAllWindows()