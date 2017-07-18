from Config import *

class Player():
    def __init__(self,image,coords,team,hasBall = False):
        self.Team = team
        self.Image = image
        self.coords = coords#x and y list
        #all_sprites_list.add(self.Image)
        self.setPosition(self.coords)
        self.HasBall = hasBall
    def Run(self,angle,distance):
        pass
    def setPosition(self,coords):
        self.Image.rect.x = coords[0]
        self.Image.rect.y = coords[1]
    def Pass(self):
        pass
