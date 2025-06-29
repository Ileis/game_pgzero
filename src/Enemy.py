import random
from pygame import Rect
from math import degrees, atan2
from Character import Character
from Projectile import Projectile
from constants import *

class Enemy(Character):
    def __init__(self, x, y, img, damage, speed, hp, speed_attack, projectile_speed, threshold):
        super().__init__(img, x, y, damage, speed, hp, speed_attack, projectile_speed)
        self._threshold = threshold
        self._clock_attack = random.random()

    def draw(self, screen):
        super().draw(screen)

    def update(self, dt, pos, characters):
        super().update(dt)
        self._animate()
        self.angle = self._angle_to_pos(pos)
        self._walk_to_player(pos, characters)
        self._avoid_overlap(characters)

    def throw_projectile(self, pos) -> Projectile | None:
        return super().throw_projectile(pos, 'projectile_enemy')

    def _animate(self):
        if self.change_frame():
            self._frame_img = 1 if self._frame_img == 2 else 2

        self._fix_image()

    def _fix_image(self):
        self.image = f'enemy_01_f{self._frame_img}'

    def _can_move(self, future_pos, characters: list[Character]) -> bool:
        for character in characters:
            if self != character and future_pos.colliderect(character._rect):
                return False
        return True

    def _avoid_overlap(self, characters):
        for character in characters:
            if self == character:
                continue

            dx = character.x - self.x
            dy = character.y - self.y
            dist = max(1, dx ** 2 + dy ** 2) ** 0.5

            if dist < self._collision_radius:
                repel_force = (self._collision_radius - dist) / self._collision_radius
                self.x -= (dx / dist) * repel_force * self._push_force
                self.y -= (dy / dist) * repel_force * self._push_force

    def _walk_to_player(self, pos, characters):
        dx = pos[0] - self.x
        dy = (HEIGHT - self._threshold) - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        x = self.x
        y = self.y

        if dist > 0:
            mov_dist = min(self._speed, dist)
            future_pos = x + (dx / dist) * mov_dist, y + (dy / dist) * mov_dist
            temp_rect = Rect(future_pos, (self.width, self.height))

            if self._can_move(temp_rect, characters):
                self.x += (dx / dist) * mov_dist
                self.y += (dy / dist) * mov_dist

    def _angle_to_pos(self, pos) -> float:
        dx, dy = pos[0] - self.x, pos[1] - self.y
        return degrees(atan2(-dy, dx)) + 90