import pygame
from Ball import Ball
from Block import Block
from Team import Team
from Match import Match
from Setup import *
from Globals import Globals

vectorPlayer = team2.Players[0]


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    Globals.sprites_list.update()
    Globals.sprites_list.draw(Globals.screen)
    clock.tick(20)
    pygame.display.flip()
    vectorPlayer.Move()
 
pygame.quit()
