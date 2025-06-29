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

        self.generate_enemy_01()
        self.generate_enemy_01()

    @property
    def enemies(self):
        return self._enemies[:]

    def draw(self):
        self.projectile_manager.draw()

        for enemy in self._enemies:
            enemy.draw()

    def update(self, dt):
        self.projectile_manager.update([self.player])

        for enemy in self._enemies:
            if not enemy.is_alive():
                self._enemies.remove(enemy)
            else:
                enemy.update(dt, self.player.pos)
                self.projectile_manager.new_projectile(enemy.throw_projectile(self.player.pos))

    def generate_enemy_01(self):
        x = random.randint(0, int(WIDTH))
        self._enemies.append(Enemy(x, 0, *bestiary[20]))

    def generate_enemies(self, qtd: int):
        for i in range(qtd):
            self._enemies.append(Enemy())

    def generate_random_enemie(self):
        return Enemy()