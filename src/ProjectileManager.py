from Manager import Manager
from Projectile import Projectile

class ProjectileManager(Manager):
    projectiles: list[Projectile]

    def __init__(self):
        self.projectiles = []

    def new_projectile(self, projectile):
        if projectile is not None:
            self.projectiles.append(projectile)

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()

    def update(self):
        for projectile in self.projectiles:
            projectile.update()
            if projectile.out_of_screen():
                self.projectiles.remove(projectile)