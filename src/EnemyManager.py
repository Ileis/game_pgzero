from Manager import Manager
from Enemy import Enemy
from Player import Player
from ProjectileManager import ProjectileManager
from bestiary import bestiary

class EnemyManager(Manager):
    enemies: list[Enemy]
    player: Player
    projectile_manager: ProjectileManager

    def __init__(self, player):
        self.player = player
        self.projectile_manager = ProjectileManager()
        self.enemies = []

        self.generate_enemy_01()

    def draw(self):
        self.projectile_manager.draw()

        for enemy in self.enemies:
            enemy.draw()

    def update(self, dt):
        self.projectile_manager.update()

        for enemy in self.enemies:
            enemy.update(dt, self.player.pos)
            self.projectile_manager.new_projectile(enemy.throw_projectile(self.player.pos))

    def generate_enemy_01(self):
        self.enemies.append(Enemy(250, 250, *bestiary[20]))

    def generate_enemies(self, qtd: int):
        for i in range(qtd):
            self.enemies.append(Enemy())

    def generate_random_enemie(self):
        return Enemy()