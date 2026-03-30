import cv2
import numpy as np


class VideoProcessor:
    def process(self, frame):
        negative = cv2.bitwise_not(frame)
        combined = np.hstack((frame, negative))
        return combined