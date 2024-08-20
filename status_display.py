from constants import *
import pygame


class Textbox():
    def __init__(self, text, font, size, x, y):
        self.text = text
        self.font = font
        self.size = size
        self.x_position = x
        self.y_position = y
    
    def draw():
        pass
    def update():
        pass


def display_menu(screen):
    pygame.font.init()
    game_font = pygame.font.Font(None, 36)
    text1 = game_font.render("ASTEROID MAYHAM!", True, "white")
    return screen.blit(text1, (SCREEN_WIDTH /2,SCREEN_HEIGHT - 40))