import pygame

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
 
