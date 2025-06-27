from pygame import Rect
from Entity import Entity
from Player import Player
from GameManager import GameManger
from constants import *

game = GameManger()

def update(dt):
    game.update(keyboard, dt)

def draw():
    game.draw(screen)

def on_mouse_move(pos):
    game.on_mouse_move(pos)

def on_mouse_down(pos, button):
    game.on_mouse_down(pos, button, mouse)