import cv2
import mediapipe as mp
import time

class HandDetection:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con
        
        self.mp_drawing = mp.solutions.drawing_utils #for visualizing landmarks
        self.mp_drawing_styles = mp.solutions.drawing_styles #for drawing landmarks
        self.mp_hands = mp.solutions.hands #detects the hands in video
        self.hands = self.mp_hands.Hands(static_image_mode=self.mode, max_num_hands = self.max_hands,
                                         min_detection_confidence=self.detection_con, min_tracking_confidence=self.track_con) # need to define parameters since I am using modular programming
        
    def findHands(self, image, draw = True):
        image.flags.writeable = draw
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image) #detect hands from camera
        
        #draw the hands annotation on camera
        if draw:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) #flip colour back to bgr to draw landmarks
            if self.results.multi_hand_landmarks:
                for hand_landmarks in self.results.multi_hand_landmarks: #for each handlandmark detect, draw them
                    self.mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style()
                    )
            return image        
                    
      
    def findPosition(self, image, handNo=0, draw=True):
        
        #landmark list
        lmList = []
        if self.results.multi_hand_landmarks:
            currentHand = self.results.multi_hand_landmarks[handNo]
            for id, landmark in enumerate(currentHand.landmark): # for each hand landmar get location and id
                #print(id, landmark)
                h,w,c = image.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(image, (cx, cy), 5, (255, 0, 255), -1)  
        return lmList
    
def main():
    #video capture set up
    cap = cv2.VideoCapture(0)
    #set up time functions for fps
    pTime = 0
    cTime = 0
    detector = HandDetection()
    while cap.isOpened():
        success, image = cap.read()
        image = detector.findHands(image)
        lmList = detector.findPosition(image)
        if len(lmList) != 0:
            print(lmList[4])
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        if not success:
            print("Camera is not working properly")
            continue
        image = cv2.flip(image, 1) #flip camera input before putting landmarks and fps
        cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255,), 2)
        cv2.imshow('MediaPipe Hands', image) 
        if cv2.waitKey(1) == ord('q'):
            break
        

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
        
        