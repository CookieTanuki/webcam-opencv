from PyQt6.QtCore import QThread, pyqtSignal

from .capture import VideoCapture
from .processor import VideoProcessor


class VideoWorker(QThread):
    frame_ready = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.running = True

        self.capture = VideoCapture()
        self.processor = VideoProcessor()

    def run(self):
        while self.running:
            frame = self.capture.read()

            if frame is None:
                continue

            processed = self.processor.process(frame)
            self.frame_ready.emit(processed)

        self.capture.release()

    def stop(self):
        self.running = False
        self.wait()
