class Clock:
    _timer: float
    _clock: float

    def __init__(self, timer):
        self._timer = timer
        self._clock = timer

    @property
    def clock(self):
        return self._clock

    @property
    def timer(self):
        return self._timer

    @clock.setter
    def clock(self, number):
        self._clock = min(self._timer, number)

    def init_clock(self):
        self._clock = 0

    def update_clock(self, dt):
        if self._clock == self._timer:
            return
        self.clock += dt

    def is_clock_ended(self):
        return self.clock == self.timer