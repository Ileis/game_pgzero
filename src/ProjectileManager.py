from Manager import Manager
from Projectile import Projectile
from Chacacter import Character

class ProjectileManager(Manager):
    projectiles: list[Projectile]

    def __init__(self):
        self.projectiles = []

    def new_projectile(self, projectile):
        if projectile is not None:
            self.projectiles.append(projectile)

    def _collision(self, characters: list[Character]):
        for projectile in self.projectiles:
            for character in characters:
                if projectile.colliderect(character):
                    character.take_damage(projectile.damage)
                    self.projectiles.remove(projectile)
                    break

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()

    def update(self, character):
        self._collision(character)

        for projectile in self.projectiles:
            projectile.update()
            if projectile.out_of_screen():
                self.projectiles.remove(projectile)