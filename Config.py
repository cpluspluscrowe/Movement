import pygame
import random

BLACK = (0, 0, 0)# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

pygame.init() #Game details
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
all_sprites_list = pygame.sprite.Group()

positions = [[20,20],[270,540],[540,0]]
hasBall = [True,False,False]
team1 = Team([],"Blue")
for i in range(3):
    player = Player(Block(BLUE),[positions[i][0],positions[i][1]],"Blue",hasBall[i])
    all_sprites_list.add(player.Image)
    team1.AddPlayer(player)
team2 = Team([],"Red")
player = Player(Block(RED),[270,270],"Red")
team2.AddPlayer(player)
match = Match(team1,team2)
ball = Ball(Block(BLACK,10),[30,30])
done = False
clock = pygame.time.Clock()
