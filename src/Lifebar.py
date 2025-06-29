from pygame import Rect
from constants import *

class Lifebar:
    _hp: int
    _frame: Rect

    def __init__(self, x, y, hp):
        self._frame = Rect(x, y + 5, *LIFEBAR)
        self._hp = hp

    def draw(self, screen):
        screen.draw.rect(self._frame, WHITE)

    def update(self, pos):
        self._fix_pos(pos)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, number):
        self._hp = max(0, number)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self) -> bool:
        return self.hp > 0

    def _fix_pos(self, pos):
        x, y = pos
        self._frame.x = x
        self._frame.y = y
