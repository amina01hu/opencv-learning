import time
import numpy as np
import cv2
import math
from hand_tracking_project.hand_tracking_modules import HandDetection
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume




def main():
    """ create project for adjusting volume controls"""
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    ############################## PYCAW IMPORTS
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    # volume.GetMute()
    # volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    ############################
    
    minVol = volRange[0]
    maxVol = volRange[1]
    vol = 0
    volBar = 400
    volPer = 0
    
    detector = HandDetection(detection_con=0.7) #changing detection confidence to have smoother tracking
    
    while cap.isOpened():
        
        success, image = cap.read()
        
        image = detector.findHands(image)
        lmList = detector.findPosition(image, draw=False)
        if len(lmList) != 0: 
            
            x1, y1 = lmList[4][1:]
            x2, y2 = lmList[8][1:]
            cx, cy = (x1 + x2)//2, (y1 + y2)//2 # double backslash to round to an interger & get center of line
            
            cv2.circle(image, (x1, y1), 5, (255, 0, 255), -1) # draw circle on two points
            cv2.circle(image, (x2, y2), 5, (255, 0, 255), -1)
            
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.circle(image, (cx, cy), 8, (255, 0, 255), -1) # draw center circle
            
            length = math.hypot(x2 - x1, y2 - y1)
            #print(length)
            # Hand range 50 - 300
            # Vol Range -65 - 0
            
            vol = np.interp(length, [30, 230], [minVol, maxVol]) # interp used to change range based on numbers needed
            volBar = np.interp(length, [30, 230], [400, 150])
            volPer = np.interp(length, [30, 230], [0, 100])
            volume.SetMasterVolumeLevel(vol, None)
            
            if length < 30: 
                cv2.circle(image, (cx, cy), 8, (0, 255, 0), -1) # draw center circle
                
        
       
        
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        image = cv2.flip(image, 1) 
        cv2.rectangle(image, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 255, 0), -1)
        cv2.putText(image, "FPS: " + str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.putText(image,  str(int(volPer)) + "%", (50,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Volume Control", image)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
        
    
    
if __name__ == "__main__":
    main()