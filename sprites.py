import pygame
from Ball import Ball
from Block import Block
from Team import Team
from Match import Match
from Setup import *




# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    clock.tick(20)
    pygame.display.flip()
    for player in match.AllPlayers:
        if player.HasBall == True:
            player.Pass()
 
pygame.quit()
