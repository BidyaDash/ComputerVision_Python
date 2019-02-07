"""FOR CONTINUOS MOVEMENT OF VEHICLES and PARKING SYSTEMS"""
import http.client, urllib
import cv2
import numpy as np
import time
sleep = 6 
key = 'BE3LC8I8YMAZ7AP2'
cap=cv2.VideoCapture("images/parkinglot2.mp4")
cap1=cv2.VideoCapture("images/parkinglot2.mp4")
#out1=cv2.VideoWriter('INPUT FRAME2.avi',-1,20.0,(512,512))
#out2=cv2.VideoWriter('BACKGROUND2.avi',-1,20.0,(512,512))
#out3=cv2.VideoWriter('DIFFERENCE BETWEEN ACCUMULATOR AND BACKGROUND2.avi',-1,20.0,(512,512))
out4=cv2.VideoWriter('THRESHOLDED2.avi',-1,20.0,(512,512))

_,f=cap.read()
f=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
th=np.zeros([512,512],dtype=np.uint8)
w=b=0

start=round(time.clock())
while cv2.waitKey(1)!=13:
    ret1,frame1=cap1.read()
    
    if not ret1:
        break
    frame1=cv2.resize(frame1,(512,512))
    frame1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    check=round(time.clock())
    if (check-start)%60==0:
        bg1=frame1
        average1=np.float32(bg1)
    if (check-start)%60>55 :
        w=w+(th==255).sum()    #np.count_nonzero(th==255)
        b=b+(th==0).sum()
        
    #cv2.imshow("INITIAL BACKGROUND",bg1)
    
    cv2.accumulateWeighted(frame1, average1, 0.01)
    bg = np.uint8(average1)
    #cv2.imshow("INPUT",frame1)
    #out1.write(frame1)
    #cv2.imshow("BACKGROUND",bg)
    #out2.write(bg)
    diff1=cv2.subtract(bg,bg1)
    #out3.write(diff1)
    #cv2.imshow("DIFFERENCE BETWEEN THE INITIAL BG AND ACCUMULATOR",diff1)    
    #th=cv2.adaptiveThreshold(diff1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,15)
    ret2,th=cv2.threshold(diff1, 80, 255 ,cv2.THRESH_BINARY)
    cv2.imshow("DIFFERENCE FRAME THRESHOLDED",th)
    out4.write(th)
end=round(time.clock())
print(end-start)
a=(w/(w+b))*100
print("White pixel density is : "+str(a)+" %")


if a>1:
    Temp1 = 8  
    params = urllib.parse.urlencode({'field1':Temp1 , 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print (Temp1)
        #print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")
        
    print("ACCIDENT")
else:
    print("NOTHING AS SUCH")
cv2.destroyAllWindows()
#out1.release()
#out2.release()
#out3.release()
out4.release()
cap.release()
cap1.release()

