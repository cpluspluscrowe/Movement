import pygame
from Config import *

class Globals():
    sprites_list = pygame.sprite.Group()
    pygame.init() #Game details
    screen = pygame.display.set_mode([screen_width, screen_height])  
    screen.fill(WHITE)
    player_list = []
    @staticmethod
    def StartGame():
        pass




