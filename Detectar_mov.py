import numpy as np
import cv2 as cv

def movimiento(I1,I2):
    if I1.shape==I2.shape:
        D = abs(I1.astype('int')-I2.astype('int'))
        D = D.astype('uint8')
        return D


w_cam = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX
if w_cam.isOpened():
    b, frame1 = w_cam.read()
    b, frame2 = w_cam.read()
    while True: 
        if b:
            Diff = movimiento(frame1,frame2)
            c = cv.Canny(Diff,150,150)
            areaBlanca = cv.findContours(c, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)[0]
            for contorno in areaBlanca:
                x,y,w,h = cv.boundingRect(contorno)
                frame1 = cv.putText(frame1,'$$',(x,y),font,1,(255,0,0),1,cv.LINE_AA)
            cv.imshow('No te muevas',frame1)
            cv.imshow('No',Diff)
            if cv.waitKey(5)==ord('q'):
                break
            frame1 = frame2
            b, frame2 = w_cam.read()
w_cam.release()
cv.destroyAllWindows()

