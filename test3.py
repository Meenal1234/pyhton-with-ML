import cv2
import time
cam=cv2.VideoCapture(0)
time.sleep(2)
face=cv2.CascadeClassifier('/lib64/python3.4/site-packages/cv2/data/haarcascade_frontalface_default.xml')
while(1):
	d,img=cam.read()
	q,r,e=img.shape
	print(q,r,e)
	cv2.imshow('my image',img)
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('my image1',gray)
	faces=face.detectMultiScale(gray,1.3,9)
	#,b=faces.shape
	#rint('umber of faces are ',a)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
	cv2.imshow('my image',img)
	k=cv2.waitKey(5) & 0xFF
	if k==27:
	   break
cv2.destroyAllWindows()

