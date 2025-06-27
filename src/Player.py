from pgzero.actor import Actor
from Entity import Entity
from Projectile import Projectile
from constants import *

class Player(Entity):
    _staff: Actor
    _direction: str

    _jump_strength: int
    _jumping: bool

    _projectile_speed: int
    _clock: int

    def __init__(self, x, y):
        super().__init__('player_f1_left', x, y)
        self._staff = Actor('staff', self.pos)

        self._clock = 0

        self._projectile_speed = 5
        self._damage = 5
        
        self._direction = LEFT
        self._frame_img = 1

        self._vel_y = 0
        self._jump_strength = -10
        self._jumping = False

    def walk_left(self):
        self.x -= self._speed
        self._norm_player()
        self._direction = LEFT

    def walk_right(self):
        self.x += self._speed
        self._norm_player()
        self._direction = RIGHT

    def jump(self):
        if not self._jumping:
            self._jumping = True
            self._vel_y = self._jump_strength
        else:
            self._vel_y += GRAVITY
            self.y += self._vel_y

            if self.y >= FLOOR - self.height / 2:
                self.y = FLOOR - PLAYER_HIGHT / 2
                self._vel_y = 0
                self._jumping = False

    def draw(self):
        super().draw()
        self._staff.draw()

    def update(self, keyboard, dt):
        self._animate(dt)

        if keyboard.space or self._jumping:
            self.jump()

        if keyboard.d:
            self.walk_right()

        if keyboard.a:
            self.walk_left()

    def angle_staff(self, pos):
        self._staff.angle = self._staff.angle_to(pos) - 90

    def throw_projectile(self, pos) -> Projectile:
        return Projectile('projectile', self.x, self.y, self._damage, self._projectile_speed, pos)

    def _norm_player(self):
        self.x = max(self.width / 2, min(WIDTH - self.width / 2, self.x))

    def _animate(self, dt):
        self._fix_image_player_direction_action()
        self._clock += dt
        if self._clock >= FRAME_RATE:
            self._clock = 0
            self._frame_img = 1 if self._frame_img == 2 else 2
            self._fix_image_player_direction_action()

    def _fix_image_player_direction_action(self):
        self._staff.pos = self.pos

        if self._jumping:
            self.image = f'player_jumping_{self._direction}'
        else:
            self.image = f'player_f{self._frame_img}_{self._direction}'