from Config import *

class Player():
    def __init__(self,image,coords,team):
        self.Team = team
        self.Image = image
        self.coords = coords
        self.setPosition(self.coords)
    def Run(self,angle,distance):
        pass
    def setPosition(self,coords):
        self.Image.rect.x = coords[0]
        self.Image.rect.y = coords[1]
    def Pass(self):
        pass
