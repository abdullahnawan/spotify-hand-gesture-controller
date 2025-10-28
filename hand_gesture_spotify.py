# Spotify Hand Gesture Controller with Accuracy Testing
import os
from dotenv import load_dotenv
import cv2
import time
import mediapipe as mp
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import deque

load_dotenv("secrets.env")

# ----- Spotify Setup ----- #
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-playback-state user-modify-playback-state user-read-currently-playing"
))

# ----- MediaPipe Setup ----- #
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
last_action_time = 0
gesture_buffer = deque(maxlen=5)

# ----- Accuracy Tracking ----- #
total_tests = 0
correct_detections = 0
expected_gesture = None

gesture_key_map = {
    ord('1'): 'palm',
    ord('2'): 'right',
    ord('3'): 'left',
    ord('4'): 'up',
    ord('5'): 'down',
    ord('0'): 'none'
}

# ----- Spotify Controls ----- #
def toggle_play_pause():
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

def volume_change(direction):
    playback = sp.current_playback()
    if playback:
        device_id = playback['device']['id']
        current_volume = playback['device']['volume_percent']
        new_volume = max(0, min(100, current_volume + (10 if direction == "up" else -10)))
        sp.volume(new_volume, device_id=device_id)

# ----- Gesture Detection Helpers ----- #
def get_finger_status(landmarks):
    return [
        abs(landmarks[4].x - landmarks[2].x) > 0.05,
        landmarks[8].y < landmarks[6].y,
        landmarks[12].y < landmarks[10].y,
        landmarks[16].y < landmarks[14].y,
        landmarks[20].y < landmarks[18].y
    ]

def detect_gesture(landmarks):
    fingers = get_finger_status(landmarks)
    thumb, index, middle, ring, pinky = fingers
    wrist = landmarks[0]
    thumb_tip = landmarks[4]

    if not any(fingers):
        return "none"
    if all(fingers):
        return "palm"

    dx = thumb_tip.x - wrist.x
    dy = thumb_tip.y - wrist.y

    if abs(dx) > abs(dy):
        if dx > 0.2:
            return "right"
        elif dx < -0.2:
            return "left"
    else:
        if dy < -0.2:
            return "up"
        elif dy > 0.2:
            return "down"

    return "none"

# ----- Main Loop ----- #
print("Gesture Control Active | Press 1=palm, 2=right, 3=left, 4=up, 5=down, 0=none")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark
            gesture = detect_gesture(lm)

    gesture_buffer.append(gesture)
    consistent_gesture = max(set(gesture_buffer), key=gesture_buffer.count) if gesture_buffer else None

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key in gesture_key_map:
        expected_gesture = gesture_key_map[key]
        total_tests += 1
        if consistent_gesture == expected_gesture:
            correct_detections += 1
        print(f"Expected: {expected_gesture}, Detected: {consistent_gesture}, Accuracy: {correct_detections}/{total_tests} ({(correct_detections/total_tests)*100:.1f}%)")

    if consistent_gesture and consistent_gesture != "none" and (time.time() - last_action_time > 2):
        try:
            if consistent_gesture == "palm":
                toggle_play_pause()
            elif consistent_gesture == "right":
                sp.next_track()
            elif consistent_gesture == "left":
                sp.previous_track()
            elif consistent_gesture == "up":
                volume_change("up")
            elif consistent_gesture == "down":
                volume_change("down")
        except Exception as e:
            print("Spotify command failed:", e)

        last_action_time = time.time()
        gesture_buffer.clear()

    cv2.putText(frame, f"Gesture: {consistent_gesture if consistent_gesture else 'None'}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Spotify Hand Control (Testing Mode)", frame)

cap.release()
cv2.destroyAllWindows()

if total_tests > 0:
    final_accuracy = (correct_detections / total_tests) * 100
    print(f"\nFinal Accuracy: {correct_detections}/{total_tests} ({final_accuracy:.2f}%)")
