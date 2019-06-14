import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,1200)
background_sub=cv2.createBackgroundSubtractorMOG2(10,400,True)
frame_count=0
while (cap.isOpened()):
	ret,frame=cap.read()
	if ret==True:
		frame_count+=1
		bg_mask=background_sub.apply(frame)
		count=np.count_nonzero(bg_mask)
		#print(count)
		if (frame_count > 1 and count > 1000):
			cv2.putText(frame, 'motion detected', (650, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
			
		cv2.imshow('Frame', frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break;
cap.release()
cv2.destroyAllWindows()
