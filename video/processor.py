import cv2
import numpy as np


class VideoProcessor:
    def __init__(self):
        self.effect = "None"

    def set_effect(self, effect):
        self.effect = effect

    def process(self, frame):
        if self.effect == "Negative":
            processed = cv2.bitwise_not(frame)
        elif self.effect == "Grayscale":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            processed = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif self.effect == "GaussianBlur":
            processed = cv2.GaussianBlur(frame, (15, 15), 0)
        elif self.effect == "EdgeDetection":
            edges = cv2.Canny(frame, 100, 200)
            processed = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif self.effect == "Sepia":
            base = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            kernel = np.array([
                [0.393, 0.769, 0.189],
                [0.349, 0.686, 0.168],
                [0.272, 0.534, 0.131]
            ])
            sepia = cv2.transform(base, kernel)
            sepia = np.clip(sepia, 0, 255)
            processed = cv2.cvtColor(sepia, cv2.COLOR_RGB2BGR)
        else:
            processed = frame

        return np.hstack((frame, processed))
