from Entity import Entity
from Projectile import Projectile
from Lifebar import Lifebar
from constants import *

class Character(Entity):
    _attack_speed: int
    _projectile_speed: int
    _clock_animate: int
    _clock_attack: int
    _frame_img: int
    lifebar: Lifebar

    def __init__(self, img, x, y, damage, speed, hp, speed_attack, projectile_speed):
        super().__init__(img, x, y, damage, speed)
        self.lifebar = Lifebar(self.center[0] - LIFEBAR[0] / 2, 5 + (self.y + self.height / 2), hp)
        self._speed_attack = speed_attack
        self._projectile_speed = projectile_speed

        self._animate_clock = 0
        self._clock_attack = 0
        self._frame_img = 1

    def update(self, dt):
        self._cooldown_attack(dt)
        self._timer_animate(dt)
        self.lifebar.update((self.center[0] - LIFEBAR[0] / 2, 5 + (self.y + self.height / 2)))

    def draw(self, screen):
        super().draw()
        self.lifebar.draw(screen)

    def attack_avaliable(self) -> bool:
        return self._clock_attack == 0

    def change_frame(self) -> bool:
        return self._animate_clock == 0

    def throw_projectile(self, pos, img_projectile) -> Projectile | None:
        if self.attack_avaliable():
            self._clock_attack = self._speed_attack
            return Projectile(img_projectile, self.x, self.y, self._damage, self._projectile_speed, pos)
        return None

    def _timer_animate(self, dt) -> bool:
        self._animate_clock += dt
        if self._animate_clock >= FRAME_RATE:
            self._animate_clock = 0
            return True
        return False

    def _cooldown_attack(self, dt):
        if self._clock_attack == 0:
            return

        self._clock_attack -= dt
        if self._clock_attack <= 0:
            self._clock_attack = 0