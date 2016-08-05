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

class Match():
    def __init__(self,team1,team2):
        self.Team1 = team1
        self.Team2 = team2
        self.AllPlayers = team1.Players + team2.Players #append lists together
class Team():
    def __init__(self,players,color):
        self.Players = players
        self.Color = color
    def AddPlayer(self,player):
        self.Players.append(player)
    def Pass(self,passingPlayer,receivingPlayer,ball):
        passingPlayer.HasBall = False
        receivingPlayer.HasBall = True
        ball.Move(orig,dest)
class Ball():
    def __init__(self,image,coords):
        self.Image = image
        self.coords = coords
        all_sprites_list.add(self.Image)
        self.setPosition(self.coords)
    def setPosition(self,coords):
        print(coords)
        self.Image.rect.x  = coords[0] #Notice not self, just in case we want to pass something in
        self.Image.rect.y = coords[1] 
class Player():
    def __init__(self,image,coords,team,hasBall = False):
        self.Team = team
        self.Image = image
        self.coords = coords#x and y list
        all_sprites_list.add(self.Image)
        self.setPosition(self.coords)
        self.HasBall = hasBall
        print(self.HasBall)
    def Run(self,angle,distance):
        pass
    def setPosition(self,coords):
        self.Image.rect.x = coords[0]
        self.Image.rect.y = coords[1]
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self,color,size = 20):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((size, size))
        self.image.fill((255,255,255))
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = pygame.draw.circle(self.image, color, (int(size/2), int(size/2)), int(size/2), 0)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        #self.rect.center = (random.randrange(-300, -20),random.randrange(0, screen_width))
 
    def update(self):
        """ Called each frame. """
 
        # Don't move for now
        #self.rect.center = (self.rect.center[0]+random.randrange(-3,3),self.rect.center[1]+random.randrange(-3,3))
 
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
score = 0
 
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
