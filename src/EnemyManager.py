import random
from Manager import Manager
from Enemy import Enemy
from Player import Player
from ProjectileManager import ProjectileManager
from bestiary import bestiary
from constants import *

class EnemyManager(Manager):
    _enemies: list[Enemy]
    player: Player
    projectile_manager: ProjectileManager

    def __init__(self, player):
        self.player = player
        self.projectile_manager = ProjectileManager()
        self._enemies = []

    def is_round_active(self) -> bool:
        return len(self._enemies) > 0

    @property
    def enemies(self):
        return self._enemies[:]

    def draw(self, screen):
        self.projectile_manager.draw()

        for enemy in self._enemies:
            enemy.draw(screen)

    def update(self, sounds, dt):
        self.projectile_manager.update([self.player], sounds)

        for enemy in self._enemies:
            if not enemy.lifebar.is_alive():
                self._enemies.remove(enemy)
            else:
                enemy.update(dt, self.player.pos, self._enemies)
                self.projectile_manager.new_projectile(enemy.throw_projectile(self.player.pos, sounds))

    def generate_enemy_01(self):
        x = random.randint(0, int(WIDTH))
        self._enemies.append(Enemy(x, 0, *bestiary[20]))

    def generate_enemies(self, qtd: int):
        for i in range(qtd):
            self.generate_enemy_01()