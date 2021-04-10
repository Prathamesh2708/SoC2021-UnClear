import numpy as np 
import cv2


def pencilshade(frame):
	frame = cv2.resize(frame , (720,540))
	frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

	dark = cv2.adaptiveThreshold(frame ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
			cv2.THRESH_BINARY,9,1)
	dark = cv2.GaussianBlur(dark , (111,111) , 0)
	dark = 255 - cv2.subtract(dark,frame)

	light = cv2.GaussianBlur(frame , (111,111), 0)
	light = 255- cv2.subtract(light, frame)

	final = light//2 + dark//2
	final = cv2.GaussianBlur(final, (3,3),0)
	return final



frame = cv2.imread("assignment1.png")
final = pencilshade(frame)

cv2.imshow("final",final)
	
cv2.waitKey(0)
cv2.destroyAllWindows()

camera = cv2.VideoCapture(0)

while camera.isOpened():
	ret ,frame = camera.read()
	final = pencilshade(frame)

	cv2.imshow("final",final)

	if cv2.waitKey(10)==27:
		break
cv2.destroyAllWindows()





