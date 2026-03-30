import cv2


class VideoCapture:
    def __init__(self, src=0, width=640, height=480):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(3, width)
        self.cap.set(4, height)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open webcam")

    def read(self):
        ret, frame = self.cap.read()

        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()
