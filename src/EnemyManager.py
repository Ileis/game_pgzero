from Manager import Manager
from Enemy import Enemy
from Player import Player
from bestiary import bestiary

class EnemyManager(Manager):
    enemies: list[Enemy]
    player: Player

    def __init__(self, player):
        self.player = player
        self.enemies = []

        self.generate_enemy_01()

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

    def update(self):
        for enemy in self.enemies:
            enemy.update(self.player.pos)

    def generate_enemy_01(self):
        self.enemies.append(Enemy(250, 250, *bestiary[20]))

    def generate_enemies(self, qtd: int):
        for i in range(qtd):
            self.enemies.append(Enemy())

    def generate_random_enemie(self):
        return Enemy()