class Ball():
    def __init__(self,image,coords):
        self.Image = image
        self.coords = coords
        all_sprites_list.add(self.Image)
        self.setPosition(self.coords)
    def setPosition(self,coords):
        print(coords)
        self.Image.rect.x  = coords[0] #Notice not self, just in case we want to pass something in
        self.Image.rect.y = coords[1] 
