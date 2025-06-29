from pygame import Rect
from GameManager import GameManager
from constants import *
import globals

class Game:
    game_manager: GameManager
    start_button: Rect
    sound_button: Rect
    exit_button: Rect

    def __init__(self, sounds):
        self.game_manager = None
        self.start_button = Rect((WIDTH / 2 - BOX_SIZE_MENU[0] / 2, (HEIGHT / 2) - BOX_SIZE_MENU[1] * 1.5 - 5) , BOX_SIZE_MENU)
        self.sound_button = Rect((WIDTH / 2 - BOX_SIZE_MENU[0] / 2, (HEIGHT / 2) - BOX_SIZE_MENU[1] * 0.5), BOX_SIZE_MENU)
        self.exit_button = Rect((WIDTH / 2 - BOX_SIZE_MENU[0] / 2, (HEIGHT / 2) + BOX_SIZE_MENU[1] * 0.5 + 5), BOX_SIZE_MENU)
        sounds.music.play()

    def draw(self, screen, clock):
        screen.clear()

        if self.game_manager is not None:
            self.game_manager.draw(screen, clock)
        else:
            sound_button_text = 'On' if globals.sound_on else 'Off'

            screen.draw.rect(self.start_button, RED)
            screen.draw.rect(self.sound_button, RED)
            screen.draw.rect(self.exit_button, RED)

            screen.draw.textbox('Start', self.start_button)
            screen.draw.textbox(f'Sound {sound_button_text}', self.sound_button)
            screen.draw.textbox('Exit', self.exit_button)

    def update(self, keyboard, sounds, dt):

        if self.game_manager is not None:
            self.game_manager.update(keyboard, dt, sounds)
        else:
            pass

    def on_mouse_move(self, pos):
        if self.game_manager is not None:
            self.game_manager.on_mouse_move(pos)
        else:
            pass
    
    def on_mouse_down(self, pos, button, mouse, sounds):
        if self.game_manager is not None:
            self.game_manager.on_mouse_down(pos, button, mouse, sounds)
        else:
            if self.start_button.collidepoint(pos):
                self.game_manager = GameManager()

            elif self.sound_button.collidepoint(pos):
                globals.sound_on = not globals.sound_on
                if globals.sound_on:
                    sounds.music.play()
                else:
                    sounds.music.stop()

            elif self.exit_button.collidepoint(pos):
                exit()
