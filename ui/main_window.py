import cv2

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

from video.worker import VideoWorker
from utils.fps_counter import FPSCounter

class MainWindow(QWidget):
    effect_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam App")

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fps_label = QLabel("FPS: 0")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.fps_label)
        self.setLayout(layout)

        self.fps_counter = FPSCounter(interval=0.2)

        self.worker = VideoWorker()
        self.worker.frame_ready.connect(self.update_frame)
        self.worker.start()

        self.effect_box = QComboBox()
        self.effect_box.addItems([
            "None",
            "Negative",
            "Grayscale",
        ])

        self.effect_changed.connect(self.worker.set_effect)
        self.effect_box.currentTextChanged.connect(self.effect_changed.emit)

        layout.addWidget(self.effect_box)

    def update_frame(self, frame):
        fps = self.fps_counter.update()
        self.fps_label.setText(f"FPS: {fps}")

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()
