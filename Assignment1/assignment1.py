import numpy as np 
import cv2

while True:
	frame = cv2.imread("assignment1.png")
	frame = cv2.resize(frame , (720,540))
	frame = cv2.pyrDown(frame)
	frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	kernel = np.ones((3,3),np.uint8)
	bnw = cv2.adaptiveThreshold(frame ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		cv2.THRESH_BINARY,9,1)
	bnw = cv2.blur(bnw , (3,3))

	gray = cv2.GaussianBlur(255-frame , (21,21), 0)
	#bnw = cv2.adaptiveThreshold(gray ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		#cv2.THRESH_BINARY,9,4)
	noisy = cv2.divide(frame,255-gray, scale =256)
	final0 = cv2.dilate(noisy , kernel, iterations = 1)
	final0 = cv2.blur(final0 ,(3,3))
	final6 = cv2.erode(noisy, kernel,iterations =1)
	cv2.imshow("a",bnw)
	cv2.imshow("noisy",noisy)
	cv2.imshow("0",final0)
	cv2.imshow("6",final6+bnw)
	cv2.imshow("new" , cv2.max(bnw,final6))
	

	if cv2.waitKey(10)==27:
		break
cv2.destroyAllWindows()





