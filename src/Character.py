from Entity import Entity
from Clock import Clock
from Projectile import Projectile
from Lifebar import Lifebar
from constants import *

class Character(Entity):
    _projectile_speed: int
    _animation: Clock
    _attack: Clock
    _frame_img: int
    _collision_radius = 30
    _push_force = 0.5
    lifebar: Lifebar

    def __init__(self, img, x, y, damage, speed, hp, attack_speed, projectile_speed):
        super().__init__(img, x, y, damage, speed)
        self.lifebar = Lifebar(self.center[0] - LIFEBAR[0] / 2, 5 + (self.y + self.height / 2), hp)
        self._projectile_speed = projectile_speed

        self._attack = Clock(attack_speed)
        self._animation = Clock(FRAME_RATE)

        self._frame_img = 1

    def update(self, dt):
        self._attack.update_clock(dt)
        self._animation.update_clock(dt)
        self._animate()
        self.lifebar.update((self.center[0] - LIFEBAR[0] / 2, 5 + (self.y + self.height / 2)))

    def draw(self, screen):
        super().draw()
        self.lifebar.draw(screen)

    def throw_projectile(self, pos, img_projectile) -> Projectile | None:
        if self._attack.is_clock_ended():
            self._attack.init_clock()
            return Projectile(img_projectile, self.x, self.y, self._damage, self._projectile_speed, pos)
        return None

    def _animate(self):
        raise NotImplementedError('_animate method not implemented')