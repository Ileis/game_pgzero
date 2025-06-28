import pgzero

from constants import *

from Manager import Manager
from SceneManager import SceneManager
from EnemyManager import EnemyManager
from ProjectileManager import ProjectileManager

from Player import Player
from Enemy import Enemy
from Projectile import Projectile

class GameManger(Manager):
    player: Player
    scene_manager: SceneManager
    enemy_manager: EnemyManager
    projectile_manager: ProjectileManager
    game_round: int

    def __init__(self):
        self.player = Player(*START_POS, *player_stats)
        self.scene_manager = SceneManager()
        self.enemy_manager = EnemyManager(self.player)
        self.projectile_manager = ProjectileManager()
        game_round = 1

    def draw(self, screen):
        self.scene_manager.draw(screen)
        self.player.draw()
        self.enemy_manager.draw()
        self.projectile_manager.draw()

    def update(self, keyboard, dt):
        self.player.update(keyboard, dt)
        self.enemy_manager.update(dt)
        self.projectile_manager.update()

    def on_mouse_move(self, pos):
        self.player.angle_staff(pos)

    def on_mouse_down(self, pos, button, mouse):
        if button == mouse.LEFT:
            self.projectile_manager.new_projectile(self.player.throw_projectile(pos))

player_stats: tuple[int, int, float, int] = (3, 2, 10, 0.5, 5)