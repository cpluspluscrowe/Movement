import pygame
from Config import *
from Team import Team
from Player import Player
from Block import Block
from Match import Match
from Ball import Ball

pygame.init() #Game details
screen = pygame.display.set_mode([screen_width, screen_height])
all_sprites_list = pygame.sprite.Group()
positions = [[20,20],[270,540],[540,0]]
team1 = Team([],"Blue")
for i in range(3):
    player = Player(Block(BLUE),[positions[i][0],positions[i][1]],"Blue")
    all_sprites_list.add(player.Image)
    team1.AddPlayer(player)
team2 = Team([],"Red")
player = Player(Block(RED),[270,270],"Red")
team2.AddPlayer(player)
match = Match(team1,team2)
ball = Ball(Block(BLACK,10),[30,30])
done = False
clock = pygame.time.Clock()
screen.fill(WHITE)
