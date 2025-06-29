from pygame import Rect
from constants import *

class Lifebar:
    _hp: int
    _frame: Rect
    _life: Rect
    _life_ratio: float

    def __init__(self, x, y, hp):
        self._frame = Rect(x, y, *LIFEBAR)
        self.hp = hp
    
        life_width = LIFEBAR[0] - 4
        life_hight = LIFEBAR[1] - 4

        self._life_ratio = life_width / max(0.1, self.hp)

        self._life = Rect(x + 2, y + 2, life_width, life_hight)

    def draw(self, screen):
        screen.draw.rect(self._frame, WHITE)
        screen.draw.rect(self._life, RED)

    def update(self, pos):
        self._fix_pos(pos)
        self._fix_life_size()

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

    def _fix_life_size(self):
        self._life.width = self.hp * self._life_ratio

    def _fix_pos(self, pos):
        self._frame.x, self._frame.y = pos
        self._life.x, self._life.y = pos[0] + 2, pos[1] + 2
