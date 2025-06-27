import pgzero
from pgzero.actor import Actor

class Entity(Actor):

    _speed: int
    _damage: int

    def __init__(self, img, x, y, damage, speed):
        super().__init__(img)
        self.pos = x, y
        self._damage = damage
        self._speed = speed

    def draw(self):
        super().draw()

    def update(self):
        raise NotImplementedError("update method not implemented")