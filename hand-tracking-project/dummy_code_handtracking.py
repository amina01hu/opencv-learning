import cv2
import mediapipe as mp
import time


mp_drawing = mp.solutions.drawing_utils #for visualizing landmarks
mp_drawing_styles = mp.solutions.drawing_styles #for drawing landmarks
mp_hands = mp.solutions.hands #detects the hands in video

#set up time functions for fps

pTime = 0
cTime = 0

#webcam setup

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    max_num_hands=1,  #change how many hands are detected
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Camera is not working properly")
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image) #detect hands from camera
        
        #draw the hands annotation on camera
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) #flip colour back to bgr to draw landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks: #for each handlandmark detect, draw them
                for id, landmark in enumerate(hand_landmarks.landmark): # for each hand landmar get location and id
                    #print(id, landmark)
                    h,w,c = image.shape
                    cx, cy = int(landmark.x*w), int(landmark.y*h)
                    tx, ty, px, py = 0, 0, 0, 0
                    print(id, cx, cy)
                    if id == 4:
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), -1)
                        tx, ty = cx, cy
                    elif id == 8:
                        cv2.circle(image, (cx, cy), 10, (255, 0, 255), -1)
                        px, py = cx, cy
                    image = cv2.line(image, (tx, ty), (px, py), (0, 255, 0), 3)
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        image = cv2.flip(image, 1) #flip camera input before putting landmarks and fps
        cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255,), 2)
        cv2.imshow('MediaPipe Hands', image) 
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
        
        