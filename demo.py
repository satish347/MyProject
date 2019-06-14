import numpy as np
import cv2
from datetime import datetime
cap = cv2.VideoCapture(0)
width=cap.get(3)
height=cap.get(4)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(width*0.75),int(height*0.75)),False)
#testing
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while(cap.isOpened()):
	ret,frame=cap.read()
	#height, width = frame.shape[:2]
	#print(height)
	#print(width)
	if ret==True:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		frame75 = rescale_frame(gray, percent=75)
		font = cv2.FONT_HERSHEY_SIMPLEX
		#Time and date added
		cv2.putText(frame75,str(datetime.now()),(10,30),font, 1,(255,255,255),2,cv2.LINE_AA)
		#rectangle value taken from cetroid of the image
		h,w=frame75.shape
		upper_left=(int(w/2-50),int(h/2-50))
		bottom_right=(int(w/2+50),int(h/2+50))
		cv2.rectangle(frame75,upper_left,bottom_right,(255,0,0),3)
		#cv2.rectangle(frame75,(384,150),(150,350),(255,0,0),3)		
		#comment added
		out.write(frame75)
		cv2.imshow('gray frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()
