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
    def setPosition(self,x=0,y=0):
        self.Image.rect.x = x
        self.Image.rect.y = y

class VectorManager():
    def __init__(self,color,x = 0, y = 0):
        self.dims = 600
        self.speed = 10
        if color == "Blue":
            self.vector = Vector(Block(BLUE),0,0)
            self.vector.move = PasserVector.move
        elif color == "Red":
            self.vector = Vector(Block(RED),-1*self.speed,-1*self.speed)
            self.vector.move = DefenderVector.move
        elif color == "Black":
            self.vector = Vector(Block(BLACK),0,0)
            self.vector.move = BallVector.move
        self.vector.setPosition(x,y)
        print(color,self.vector.vector_x,self.vector.vector_y)
    def CheckBoundaries(self):
        if self.vector.Image.rect.x > 540:
            self.vector.setX(-1*self.speed)
        if self.vector.Image.rect.x < 20:
            self.vector.setX(self.speed)
        if self.vector.Image.rect.y > 540:
            self.vector.setY(-1*self.speed)
        if self.vector.Image.rect.y < 20:
            self.vector.setY(self.speed)
    def Move(self):
        self.CheckBoundaries()
        self.vector.move(self.vector)
