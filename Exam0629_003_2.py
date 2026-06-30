import cv2 as cc
import numpy as np
cap = cc.VideoCapture("stopwatch.avi")
if not cap.isOpened(): raise Exception("오류")

fps = cap.get(cc.CAP_PROP_FPS)
delay = int(1000/fps)
writer  = cc.VideoWriter("output",cc.videoWriter_fourcc(*'mp4v'),fps)
while True:
    ret, frame = cap.read()
    if not ret : break
    inv = (frame[:,:,:] + np.array([0,0,100], dtype=np.uint8)).astype(np.uint8)
    print(inv)
    cc.imshow('frame',frame)
    cc.imshow('inverted',inv)
    key = cc.waitKey(delay)
    if  key >= 0 or key == ord('q') or key == ord("Q") : 
        break

cap.release()