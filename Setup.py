import pygame
from Config import *
from Team import Team
from Player import Player
from Block import Block
from Match import Match
from Ball import Ball
from Globals import Globals

Globals.StartGame()
positions = [[20,20],[270,540],[540,0]]
team1 = Team([],"Blue")
for i in range(3):
    player = Player([positions[i][0],positions[i][1]],"Blue")
    team1.AddPlayer(player)

team2 = Team([],"Red")
player = Player([270,270],"Red")

team2.AddPlayer(player)

match = Match(team1,team2)

ball = Ball([60,60],"Black")

done = False
clock = pygame.time.Clock()


