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
        else:
            processed = frame

        return np.hstack((frame, processed))
