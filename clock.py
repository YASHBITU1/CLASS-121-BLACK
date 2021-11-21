import cv2 
import time
import numpy as np 

output = cv2.VideoWriter_fourcc(*'XVID')
outputFile = cv2.VideoWriter('output.avi',output,20.0,(600,600))
capture = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(60):
    ret,bg = capture.read()

bg = np.flip(bg,axis= 1)

while(capture.isOpened()):
    ret,img = capture.read()
    if(not ret):
        break
    bg = np.flip(img,axis= 1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    Lred = np.array([0,120,50])
    Ured = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,Lred,Ured)
    Lred = np.array([170,120,70])
    Ured=np.array([180,255,255])
    mask2 = cv2.inRange(hsv,Lred,Ured)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    withoutRed = cv2.bitwise_and(img,img,mask = mask2)
    withRed = cv2.bitwise_and(bg,bg,mask = mask1)
    FinalOutput = cv2.addWeighted(withoutRed,1,withRed,1,0)
    outputFile.write(FinalOutput)
    cv2.imshow("magic",FinalOutput)
    cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()

