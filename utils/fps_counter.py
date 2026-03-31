import time


class FPSCounter:
    def __init__(self, interval=1):
        self.interval = interval
        self.frame_count = 0

        self.prev_time = time.time()
        self.fps = 0

    def update(self):
        self.frame_count += 1
        current = time.time()
        elapsed = current - self.prev_time

        if elapsed >= self.interval:
            self.fps = self.frame_count / elapsed
            self.frame_count = 0
            self.prev_time = current

        return int(self.fps)
