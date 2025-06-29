from pygame import Rect
from Game import Game
from Entity import Entity
from Player import Player
from constants import *


# tela de inicio
game = Game(sounds)

def update(dt):
    game.update(keyboard, sounds, dt)

def draw():
    game.draw(screen, clock)

def on_mouse_move(pos):
    game.on_mouse_move(pos)

def on_mouse_down(pos, button):
    game.on_mouse_down(pos, button, mouse, sounds)