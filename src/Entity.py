import pgzero
from pgzero.actor import Actor

class Entity(Actor):

    _speed: int
    _damage: int
    _focus: tuple[int, int]

    def __init__(self, img, x, y, focus = None):
        super().__init__(img)
        self.pos = x, y
        self._speed = 2
        self._damage = 10
        self._focus = focus

    def angle_to():
        if self._focus is not None:
            super().angle_to(focus)
