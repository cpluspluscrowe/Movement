from Vector import VectorManager

class Ball(VectorManager):
    def __init__(self,coords,color):
        super().__init__(color,coords[0],coords[1])
        self.coords = coords
