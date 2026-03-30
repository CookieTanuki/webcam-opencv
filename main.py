import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    ret, frame = cap.read()
    negative = cv2.bitwise_not(frame)
    combined = np.vstack((frame, negative))
    cv2.imshow("Webcam", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
