from Manager import Manager
from Projectile import Projectile
from Character import Character
import globals

class ProjectileManager(Manager):
    projectiles: list[Projectile]

    def __init__(self):
        self.projectiles = []

    def new_projectile(self, projectile):
        if projectile is not None:
            self.projectiles.append(projectile)

    def _collision(self, characters: list[Character], sounds):
        for projectile in self.projectiles:
            for character in characters:
                if projectile.colliderect(character):

                    if globals.sound_on:
                        sounds.character_takes_damage.play()

                    character.lifebar.take_damage(projectile.damage)
                    self.projectiles.remove(projectile)
                    break

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()

    def update(self, character, sounds):
        self._collision(character, sounds)

        for projectile in self.projectiles:
            projectile.update()
            if projectile.out_of_screen():
                if projectile.hit_the_ground():
                    if globals.sound_on:
                        sounds.projectile_hit_the_ground.play()

                self.projectiles.remove(projectile)