import cv2
import numpy as np

cap=cv2.VideoCapture('rtsp://naresh:naresh1234@sidvr1.ddns.net:554/Streaming/Channels/201')
width=cap.get(3)
height=cap.get(4)
background_sub=cv2.createBackgroundSubtractorMOG2(10,400,True)
frame_count=0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(width),int(height)))
while (cap.isOpened()):
	ret,frame=cap.read()
	if ret==True:
		frame_count+=1
		#frame75 = rescale_frame(frame, percent=75)
		bg_mask=background_sub.apply(frame)
		count=np.count_nonzero(bg_mask)
		#print(count)
		if (frame_count > 1 and count > 3000):
			cv2.putText(frame, 'motion detected', (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
		#cv2.imshow('blackFrame',bg_mask)
		cv2.imshow('Frame', frame)
		out.write(frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break;
cap.release()
cv2.destroyAllWindows()
