import cv2

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt

from video.worker import VideoWorker

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam App")

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.worker = VideoWorker()
        self.worker.frame_ready.connect(self.update_frame)
        self.worker.start()

    def update_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb.shape
        bytes_per_line = ch * w

        image = QImage(
            rgb.data,
            w,
            h,
            bytes_per_line,
            QImage.Format.Format_RGB888
        )

        self.label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.worker.stop()
        event.accept()
