import cv2  
import numpy as np  
  
output = cv2.VideoCapture(0) 
image = cv2.imread("output.jpeg") 
  
while True: 
    ret, frame = output.read() 
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  

    LBlack = np.array([30, 30, 0]) 
    UBlack = np.array([104, 153, 70]) 
    
  
    mask1 = cv2.inRange(frame, LBlack, UBlack) 
    res = cv2.bitwise_and(frame, frame, mask = mask1) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("output", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('Esc'):
        break 
  
output.release() 
cv2.destroyAllWindows() 