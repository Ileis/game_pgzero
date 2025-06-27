from Manager import Manager
from Enemy import Enemy

class EnemyManager(Manager):
    enemies: list[Enemy]

    def __init__(self):
        self.enemies = []

    def draw(self):
        for enemy in self.enemies:
            enemy.draw()

    def update(self):
        for enemy in self.enemies:
            enemy.update()