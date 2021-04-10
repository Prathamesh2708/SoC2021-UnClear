import numpy as numpy
import cv2 


image = cv2.imread("assignment1.png")
image = cv2.resize(image , (540,360))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bnw = cv2.adaptiveThreshold(gray ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		cv2.THRESH_BINARY,9,4)
bnw2 = cv2.blur(bnw,(5,5))
cv2.imshow("Original " , image)
cv2.imshow("grayscale" , gray)
cv2.imshow("Black and white" , bnw)
cv2.waitKey(0)
cv2.destroyAllWindows()
camera = cv2.VideoCapture(0)

while camera.isOpened():
	ret , frame = camera.read()
	cv2.imshow("You" ,frame)
	if cv2.waitKey(1) == 27:
		break

camera.release()
cv2.destroyAllWindows()
cv2.imshow("Original" , image)
image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
cv2.imshow("Red to Blue" , image)
cv2.waitKey(0)
cv2.destroyAllWindows()









