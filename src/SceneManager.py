from Manager import Manager
from constants import *

class SceneManager(Manager):    
    def draw(self, screen):
        screen.clear()
        screen.draw.line(START_FLOOR, END_FLOOR, WHITE)
        
    def update(self):
        pass