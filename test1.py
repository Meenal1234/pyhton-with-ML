import cv2
i=cv2.imread('/root/Desktop/index.jpg')
print(i)
cv2.imshow('image',i)
k=cv2.waitKey(0)
if(k==ord('q')):
	cv2.destroyAllWindows()

