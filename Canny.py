import cv2

cap=cv2.VideoCapture(0)

while cv2.waitKey(1)!= 13:
   ret,frame=cap.read()
   ed=cv2.Canny(frame,120,220)
   cv2.imshow("EDGES",cv2.flip(ed,1))
cap.release()  
cv2.destroyAllWindows()
