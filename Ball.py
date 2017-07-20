from Vector import VectorManager

class Ball(VectorManager):
    def __init__(self,image,coords):
        super().__init__("Black",coords[0],coords[1])
        self.coords = coords
