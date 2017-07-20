import pygame
from Config import *

class Globals():
    sprites_list = pygame.sprite.Group()
    pygame.init() #Game details
    screen = pygame.display.set_mode([screen_width, screen_height])  
    screen.fill(WHITE)
    @staticmethod
    def StartGame():
        pass




