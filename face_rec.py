import numpy as np
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,700)
face_cascade=cv2.CascadeClassifier('/home/satish/Desktop/data/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade=cv2.CascadeClassifier('/home/satish/Desktop/data/haarcascades/haarcascade_eye.xml')
while(cap.isOpened()):
	ret,frame=cap.read()
	if ret==True:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces=face_cascade.detectMultiScale(frame,1.5,5)
		for(x,y,w,h) in faces:
			roi_gray=gray[y:y+h,x:x+w]
			roi_color=frame[y:y+h,x:x+w]
			h,w=x+w,y+h
			cv2.rectangle(frame,(x,y),(h,w),(255,0,0),3)
			eyes = eye_cascade.detectMultiScale(roi_color)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('img',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
	

