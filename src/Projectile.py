from Entity import Entity
from constants import *

class Projectile(Entity):
    def __init__(self, img, x, y, damage, speed, focus = None):
        super().__init__(img, x, y, focus)
        self._damage = damage
        self._speed = speed

        self._vec = focus[0] - self.x, focus[1] - self.y
        distance = (self._vec[0] ** 2 + self._vec[1] ** 2) ** 0.5
        self._vec = self._vec[0] / distance, self._vec[1] / distance

    def update(self):
        self.x += self._vec[0] * self._speed
        self.y += self._vec[1] * self._speed

    def out_screen(self):
        return self.y < 0 or self.y > HEIGHT or self.x < 0 or self.x > WIDTH
    