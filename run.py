import cv2
import mediapipe as mp
import numpy as np
import src.extra
import joblib


WINDOW = "Hand Tracking"

connections = src.extra.connections
int_to_char = src.extra.classes

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

gesture_clf = joblib.load(r'models\\gesture_clf.pkl')

# Compatibility patch for old scikit-learn GaussianNB model
if hasattr(gesture_clf, "sigma_") and not hasattr(gesture_clf, "var_"):
    gesture_clf.var_ = gesture_clf.sigma_

cv2.namedWindow(WINDOW)
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

word = []
letter = ""
staticGesture = 0

while True:
    hasFrame, frame = capture.read()

    if not hasFrame or frame is None:
        continue

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    points = None
    joints = None

    if results.multi_hand_landmarks and len(results.multi_hand_landmarks) > 0:
        landmarks = results.multi_hand_landmarks[0]
        
        # Extract landmarks as (21, 2) array in pixel coordinates
        joints = np.array([[lm.x * w, lm.y * h] for lm in landmarks.landmark])
        points = joints
    
    if points is not None:
        src.extra.draw_points(points, frame)
        pred_sign = src.extra.predict_sign(joints, gesture_clf, int_to_char)
        if letter == pred_sign:
            staticGesture += 1
        else:
            letter = pred_sign
            staticGesture = 0
        if staticGesture > 12:
            word.append(letter)
            staticGesture = 0

    if points is None:
        try:
            if word[-1] != " ":
                staticGesture += 1
                if staticGesture > 12:
                    word.append(" ")
                    staticGesture = 0
        except IndexError:
            pass

    src.extra.draw_sign(word, frame, (50, 460))

    cv2.imshow(WINDOW, frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == 8:
        try:
            del word[-1]
        except IndexError as e:
            print(e)


capture.release()
cv2.destroyAllWindows()
