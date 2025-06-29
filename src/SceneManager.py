from Manager import Manager
from constants import *

class SceneManager(Manager):

    def __init__(self):
        pass

    def draw(self, screen, round):
        screen.clear()
        screen.draw.line(START_FLOOR, END_FLOOR, WHITE)
        
    def update(self, dt):
        pass

    def round_screen(self, round, screen):
        screen.draw.text(f'Round {round}', (WIDTH / 2, HEIGHT / 2))

    