from pygame import Rect
import pgzero
from Entity import Entity
from Player import Player
from constants import *

player = Player(keyboard, clock, *START_POS)

def update():
    player.update()

def draw():
    screen.clear()
    player.draw()
    screen.draw.line(START_FLOOR, END_FLOOR, WHITE)

def on_mouse_move(pos):
    player.angle_staff(pos)