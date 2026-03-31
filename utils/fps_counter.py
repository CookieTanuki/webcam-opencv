import time


class FPSCounter:
    def __init__(self):
        self.prev_time = time.time()
        self.fps = 0

    def update(self):
        current = time.time()
        new_fps = 1 / (current - self.prev_time)
        self.prev_time = current

        self.fps = 0.9 * self.fps + 0.1 * new_fps

        return int(self.fps)
