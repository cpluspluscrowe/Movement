from Globals import Globals
from Block import Block
from Config import *

class DefenderVector():
    @staticmethod
    def move(vector):
        vector.Image.rect.x += vector.vector_x
        vector.Image.rect.y += vector.vector_y

class BallVector():
    @staticmethod
    def move(vector):
        vector.Image.rect.x += vector.vector_x
        vector.Image.rect.y += vector.vector_y

class PasserVector():
    @staticmethod
    def move(vector):
        pass #no movement

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

class VectorManager():
    def __init__(self,color,x = 0, y = 0):
        self.dims = 600
        if color == "Blue":
            self.vector = Vector(Block(BLUE),-5,-5)
            self.vector.move = DefenderVector.move
        elif color == "Red":
            self.vector = Vector(Block(RED),0,0)
            self.vector.move = BallVector.move
        elif color == "Black":
            self.vector = Vector(Block(BLACK),0,0)
            self.vector.move = PasserVector.move
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
        self.vector.move(self.vector)
