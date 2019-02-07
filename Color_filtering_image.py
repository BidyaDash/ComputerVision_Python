import cv2
import numpy as np
img=cv2.imread('images/Sunflowers.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower=np.array([10,100,100])
upper=np.array([30,255,255])
mask=cv2.inRange(hsv,lower,upper)
res=cv2.bitwise_and(img,img,mask=mask)
k=np.array([[0,1,0],[1,0,1],[0,1,0]],np.uint8)
er=cv2.erode(res,k,iterations=1)
di=cv2.dilate(res,k,iterations=1)
op=cv2.morphologyEx(res,cv2.MORPH_OPEN,k)
cl=cv2.morphologyEx(res,cv2.MORPH_CLOSE,k)
cv2.imshow("image",img)
cv2.imshow("mask",mask)
cv2.imshow("filter",res)
cv2.imshow("erosion",er)
cv2.imshow("dilation",di)
cv2.imshow("opening",op)
cv2.imshow("closing",cl)
cv2.waitKey()
cv2.destroyAllWindows()
    
    
