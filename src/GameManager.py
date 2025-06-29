import pgzero

from constants import *

from Manager import Manager
from SceneManager import SceneManager
from EnemyManager import EnemyManager
from ProjectileManager import ProjectileManager

from Player import Player
from Enemy import Enemy
from Projectile import Projectile

class GameManager(Manager):
    player: Player
    scene_manager: SceneManager
    enemy_manager: EnemyManager
    projectile_manager: ProjectileManager
    _wave_size: int
    _game_round: int
    _clock_round: float

    def __init__(self):
        self.player = Player(*START_POS, *player_stats)
        self.scene_manager = SceneManager()
        self.enemy_manager = EnemyManager(self.player)
        self.projectile_manager = ProjectileManager()
        self._game_round = 0
        self._wave_size = 5
        self._clock_round = 0

    def draw(self, screen, clock):
        self.scene_manager.draw(screen, self._game_round)
        self.player.draw(screen)
        self.enemy_manager.draw(screen)
        self.projectile_manager.draw()

        if self._round_screen_on():
            self.scene_manager.round_screen(self._game_round, screen)

        if not self.enemy_manager.is_round_active():
            self._init_clock_round_screen()
            self.generate_wave()

    def generate_wave(self):
        self._game_round += 1
        self.enemy_manager.generate_enemies(self._wave_size)
        self._wave_size += 3

    def _clock_round_screen(self, dt):
        if self._clock_round == 0:
            return

        self._clock_round -= dt
        if self._clock_round < 0:
            self._clock_round = 0

    def _round_screen_on(self):
        return self._clock_round > 0

    def _init_clock_round_screen(self):
        self._clock_round = ROUND_SCREEN_TIME

    def update(self, keyboard, dt, sounds):
        self.player.update(keyboard, dt)
        self.enemy_manager.update(sounds, dt)
        self.projectile_manager.update(self.enemy_manager.enemies, sounds)
        self._clock_round_screen(dt)

    def on_mouse_move(self, pos):
        self.player.angle_staff(pos)

    def on_mouse_down(self, pos, button, mouse, sounds):
        if button == mouse.LEFT:
            self.projectile_manager.new_projectile(self.player.throw_projectile(pos, sounds))

player_stats: tuple[int, int, float, int] = (3, 2, 20, 0.5, 5)