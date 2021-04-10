import numpy as np 
import cv2


image= cv2.imread("assignment2.png")
image = cv2.resize(image , (250 , 250))
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
rows, cols  = gray.shape

right = np.float32([[1, 0 , rows/10 ] , [0 ,1 ,0]])
newt = cv2.warpAffine(gray , right , (cols, rows))
newr = cv2.rotate(image , cv2.ROTATE_90_CLOCKWISE)
for i in range(4):
	cv2.imshow("go right "+str(i) ,newt)
	cv2.imshow("rotated "+str(i) , newr)
	newt = cv2.warpAffine(newt , right , (cols, rows)) 
	newr = cv2.rotate(newr, cv2.ROTATE_90_CLOCKWISE)

blur = cv2.blur(image , (5,5))
cv2.imshow("blur1",blur)
gblur = cv2.GaussianBlur(image,(11,11) , 0)
cv2.imshow("gblur",gblur)


cv2.waitKey(0)
cv2.destroyAllWindows()


