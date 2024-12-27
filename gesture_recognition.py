import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2, 
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def recognize_letter(hand1_landmarks, hand2_landmarks):
    if hand1_landmarks and hand2_landmarks:
        if (hand1_landmarks[8].x < hand1_landmarks[4].x and
            hand2_landmarks[8].x > hand2_landmarks[4].x):
            return "A"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y):
            return "B"

        if (hand1_landmarks[8].x < hand1_landmarks[6].x and
            hand2_landmarks[8].x > hand2_landmarks[6].x):
            return "C"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand2_landmarks[12].y > hand2_landmarks[10].y):
            return "D"

        if (hand1_landmarks[8].y > hand1_landmarks[6].y and
            hand2_landmarks[8].y > hand2_landmarks[6].y):
            return "E"

        if (hand1_landmarks[4].x < hand1_landmarks[8].x and
            hand2_landmarks[4].x > hand2_landmarks[8].x):
            return "F"

        if (hand1_landmarks[4].y < hand1_landmarks[3].y and
            hand2_landmarks[4].y < hand2_landmarks[3].y):
            return "G"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[12].y < hand1_landmarks[10].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[12].y < hand2_landmarks[10].y):
            return "H"

        if (hand1_landmarks[20].y < hand1_landmarks[18].y and
            hand2_landmarks[20].y < hand2_landmarks[18].y):
            return "I"

        if (hand1_landmarks[20].x > hand1_landmarks[18].x or
            hand2_landmarks[20].x > hand2_landmarks[18].x):
            return "J"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[12].y < hand1_landmarks[10].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[12].y < hand2_landmarks[10].y):
            return "K"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[4].x < hand1_landmarks[3].x and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[4].x < hand2_landmarks[3].x):
            return "L"

        if (hand1_landmarks[4].y > hand1_landmarks[3].y and
            hand2_landmarks[4].y > hand2_landmarks[3].y):
            return "M"

        if (hand1_landmarks[4].y > hand1_landmarks[3].y and
            hand2_landmarks[4].y > hand2_landmarks[3].y):
            return "N"

        if (hand1_landmarks[4].x < hand1_landmarks[8].x and
            hand2_landmarks[4].x > hand2_landmarks[8].x):
            return "O"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[12].y < hand1_landmarks[10].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[12].y < hand2_landmarks[10].y):
            return "P"

        if (hand1_landmarks[4].y > hand1_landmarks[3].y and
            hand2_landmarks[8].x < hand2_landmarks[6].x):
            return "Q"

        if (hand1_landmarks[8].x < hand1_landmarks[12].x and
            hand2_landmarks[8].x < hand2_landmarks[12].x):
            return "R"

        if (hand1_landmarks[4].y < hand1_landmarks[3].y and
            hand2_landmarks[4].y < hand2_landmarks[3].y):
            return "S"

        if (hand1_landmarks[4].y > hand1_landmarks[3].y and
            hand2_landmarks[4].y > hand2_landmarks[3].y):
            return "T"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[12].y < hand1_landmarks[10].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[12].y < hand2_landmarks[10].y):
            return "U"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[12].y < hand1_landmarks[10].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[12].y < hand2_landmarks[10].y):
            return "V"

        if (hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand1_landmarks[12].y < hand1_landmarks[10].y and
            hand1_landmarks[16].y < hand1_landmarks[14].y and
            hand2_landmarks[8].y < hand2_landmarks[6].y and
            hand2_landmarks[12].y < hand2_landmarks[10].y and
            hand2_landmarks[16].y < hand2_landmarks[14].y):
            return "W"

        if (hand1_landmarks[8].x > hand1_landmarks[6].x or
            hand2_landmarks[8].x > hand2_landmarks[6].x):
            return "X"

        if (hand1_landmarks[4].x < hand1_landmarks[3].x and
            hand1_landmarks[20].y < hand1_landmarks[18].y and
            hand2_landmarks[4].x < hand2_landmarks[3].x and
            hand2_landmarks[20].y < hand2_landmarks[18].y):
            return "Y"

        if (hand1_landmarks[8].x > hand1_landmarks[6].x and
            hand1_landmarks[8].y < hand1_landmarks[6].y and
            hand2_landmarks[8].x > hand2_landmarks[6].x and
            hand2_landmarks[8].y < hand2_landmarks[6].y):
            return "Z"

    elif hand1_landmarks:
        if (hand1_landmarks[8].x < hand1_landmarks[6].x and
            hand1_landmarks[12].x < hand1_landmarks[10].x):
            return "C"

    return "Tidak Dikenali"

cap = cv2.VideoCapture(0)

print("Program dimulai. Arahkan tangan Anda ke kamera.")
print("Tekan 'q' untuk keluar.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Tidak dapat membaca dari kamera. Pastikan kamera terhubung.")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    hand_landmarks_list = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            hand_landmarks_list.append(hand_landmarks.landmark)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    letter = "Tidak Dikenali"
    if len(hand_landmarks_list) == 2:
        letter = recognize_letter(hand_landmarks_list[0], hand_landmarks_list[1])
    elif len(hand_landmarks_list) == 1:
        letter = recognize_letter(hand_landmarks_list[0], None)

    cv2.putText(frame, f"Detected: {letter}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Testing Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
