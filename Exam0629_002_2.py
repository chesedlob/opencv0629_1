import cv2 as cc
import numpy as np

cap = cc.VideoCapture(0)
if cap.isOpened() == False:raise Exception("오류")

width = int(cap.get(cc.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cc.CAP_PROP_FRAME_HEIGHT))
filename = input("파일 이름을 입력해주세요")
writer = cc.VideoWriter(filename, cc.VideoWriter_fourcc(*'mp4v'),30,(width,height))
if writer.isopend() == False:
    raise Exception("오률")

ischalcak = False
while True:
    ret, frame = cap.read()
    if not ret: break

    key = cc.waitKey(1)
    if key == ord('s'):
        ischalcak = True
    if key == ord('e'):
        ischalcak = False
    if ischalcak:
        
        writer.write(frame)
        cc.imshow("frame",frame)
    else:  
        filename = input("파일 이름을 입력해주세요")
        writer.__init__(filename,cc.videoWriter_fourcc(*'mp4v'),30,(width,height))
writer.release()
cap.release()


