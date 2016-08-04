import pygame
import random

 # Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Match():
    def __init__(self,team1,team2):
        self.Team1 = team1
        self.Team2 = team2
class Team():
    def __init__(self,players,color):
        self.Players = players
        self.Color = color
class Ball():
    def __init__(self,image):
        self.Image = image
class Player():
    def __init__(self,image,team):
        self.Team = team
        self.Image = image
        self.HasBall = False
    def Pass(self,angle,distance):
        pass
    def Run(self,angle,distance):
        pass
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self,color):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((20, 20))
        self.image.fill((255,255,255))
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = pygame.draw.circle(self.image, color, (10, 10), 10, 0)
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
 
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
#block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
positions = [[20,20],[270,540],[540,0]]
for i in range(3):
    # This represents a block
    player = Player(Block(BLACK),"Blue")
    print(positions[i])
    # Set a random location for the block
    player.Image.rect.x = positions[i][0]
    player.Image.rect.y = positions[i][1]
 
    # Add the block to the list of objects
    #block_list.add(block)
    all_sprites_list.add(player.Image)
 
# Create a red player block
player = Player(Block(RED),"Red")
player.Image.rect.x = 270
player.Image.rect.y = 270
all_sprites_list.add(player.Image)
 
done = False
 
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
 
    # See if the player block has collided with anything.
    #blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    # Check the list of collisions.
 
        # Reset block to the top of the screen to fall again.
    player.Image.reset_pos()
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
