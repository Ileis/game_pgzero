from math import degrees, atan2
from Chacacter import Character
from Projectile import Projectile
from constants import *

class Enemy(Character):
    def __init__(self, x, y, img, damage, speed, hp, speed_attack, projectile_speed, threshold):
        super().__init__(img, x, y, damage, speed, hp, speed_attack, projectile_speed)
        self._threshold = threshold

    def draw(self):
        super().draw()

    def update(self, dt, pos):
        super().update(dt)
        self._animate()
        self.angle = self._angle_to_pos(pos)
        self._walk_to_player(pos)

    def throw_projectile(self, pos) -> Projectile | None:
        return super().throw_projectile(pos, 'projectile_enemy')

    def _animate(self):
        if self.change_frame():
            self._frame_img = 1 if self._frame_img == 2 else 2

        self._fix_image()

    def _fix_image(self):
        self.image = f'enemy_01_f{self._frame_img}'

    def _walk_to_player(self, pos):
        dx = pos[0] - self.x
        dy = (HEIGHT - self._threshold) - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5

        if dist > 0:
            mov_dist = min(self._speed, dist)
            self.x += (dx / dist) * mov_dist
            self.y += (dy / dist) * mov_dist

    def _angle_to_pos(self, pos) -> float:
        dx, dy = pos[0] - self.x, pos[1] - self.y
        return degrees(atan2(-dy, dx)) + 90