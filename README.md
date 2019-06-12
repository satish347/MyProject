import cv2

def make_1080p():
	cap.set(3,1920)
	cap.set(4,1080)

def make_480p():
	cap.set(3,1280)
	cap.set(4,720)

cap = cv2.VideoCapture('/home/satish/Desktop/test_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480),True)

if(cap.isOpened() == False):
	print("error opening the file")

while(cap.isOpened()):
	ret, frame = cap.read()
	
	make_1080p()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	if frame is not None:
		cv2.imshow("video", gray)
		out.write(gray)
		if cv2.waitKey(25) & 0xFF == ord('q') :
			break


	else:
		print("Frame is none")
		break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Video Stop")
