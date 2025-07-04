import cv2
import mediapipe as mp

mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
mp_drawing=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)

while cap.isOpened():
    success,image=cap.read()
    if not success :
        print("Ignoring empty frame.")
        continue
    image=cv2.flip(image,1)
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb_image)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("HAND TRACKING",image)

    if cv2.waitKey(1) & 0xFF==ord('c'):
        break

cap.release()
cv2.destroyAllWindows()