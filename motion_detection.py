import cv2
import numpy as np

cap=cv2.VideoCapture(0)
background_sub=cv2.createBackgroundSubtractorMOG2(10,400,True)
frame_count=0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 24.0, (640,480))
while (cap.isOpened()):
	ret,frame=cap.read()
	if ret==True:
		frame_count+=1
		bg_mask=background_sub.apply(frame)
		count=np.count_nonzero(bg_mask)
		#print(count)
		if (frame_count > 1 and count > 1000):
			cv2.putText(frame, 'motion detected', (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
			
		cv2.imshow('Frame', frame)
		out.write(frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break;
cap.release()
cv2.destroyAllWindows()
