from Config import *
from Block import Block
from Globals import Globals
from Vector import VectorManager

class Player(VectorManager):
    def __init__(self,coords,color):
        super().__init__(color,coords[0],coords[1])
        self.coords = coords
        Globals.player_list.append(self)
    def Pass(self):
        pass
