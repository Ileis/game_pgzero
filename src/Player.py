from pgzero.actor import Actor
from Entity import Entity
from constants import *

class Player(Entity):
    _staff: Actor

    _jump_strength: int
    _jumping: bool

    def __init__(self, x, y):
        super().__init__('player', x, y)
        self._staff = Actor('staff', self.pos)

        self._vel_y = 0
        self._jump_strength = -10
        self._jumping = False


    def walk_left(self):
        self.x -= self._speed
        self._staff.pos = self.pos
        self.norm_player()

    def walk_right(self):
        self.x += self._speed
        self._staff.pos = self.pos
        self.norm_player()

    def jump(self):
        self._jumping = True
        self._vel_y = self._jump_strength


    def draw(self):
        super().draw()
        self._staff.draw()

    def update(self, keyboard):
        if keyboard.space and not self._jumping:
            self.jump()

        if self._jumping:
            self._vel_y += GRAVITY
            self.y += self._vel_y
            self._staff.pos = self.pos

            if self.y >= FLOOR - self.height / 2:
                self.y = FLOOR - self.height / 2
                self._vel_y = 0
                self._jumping = False

        if keyboard.d:
            self.walk_right()
        if keyboard.a:
            self.walk_left()

    def angle_staff(self, pos):
        self._staff.angle = self._staff.angle_to(pos) - 90

    def norm_player(self):
        self.x = max(self.width / 2, min(WIDTH - self.width / 2, self.x))
    