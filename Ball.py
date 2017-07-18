class Vector():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

class Ball():
    def __init__(self,image,coords):
        self.Image = image
        self.coords = coords
        self.setPosition(self.coords)
    def setPosition(self,coords):
        self.Image.rect.x  = coords[0]
        self.Image.rect.y = coords[1]
    def setVector(vector):
        self.vector = vector
