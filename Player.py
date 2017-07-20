from Config import *
from Block import Block
from Globals import Globals

class Vector():
    def __init__(self,image,vector_x,vector_y):
        self.Image = image
        Globals.sprites_list.add(self.Image)
        self.vector_x = vector_x
        self.vector_y = vector_y
    def setX(self,vector_x):
        self.vector_x = vector_x
    def setY(self,vector_y):
        self.vector_y = vector_y
    def move(self):
        self.Image.rect.x += self.vector_x
        self.Image.rect.y += self.vector_y

class VectorManager():
    def __init__(self,color,x = 0, y = 0):
        self.dims = 600
        if color == "Blue":
            self.vector = Vector(Block(BLUE),-5,-5)
        else:
            self.vector = Vector(Block(RED),-5,-5)
    def CheckBoundaries(self):
        if self.vector.Image.rect.x > 595:
            self.vector.setX(-1)
        if self.vector.Image.rect.x < 5:
            self.vector.setX(1)
        if self.vector.Image.rect.y > 595:
            self.vector.setY(-1)
        if self.vector.Image.rect.y < 5:
            self.vector.setY(1)
    def Move(self):
        self.CheckBoundaries()
        self.vector.move()
        

class Player(VectorManager):
    def __init__(self,coords,color):
        super().__init__(color,coords[0],coords[1])
        self.coords = coords
    def Pass(self):
        pass
