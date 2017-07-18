class Player():
    def __init__(self,image,coords,team,hasBall = False):
        self.Team = team
        self.Image = image
        self.coords = coords#x and y list
        all_sprites_list.add(self.Image)
        self.setPosition(self.coords)
        self.HasBall = hasBall
        print(self.HasBall)
    def Run(self,angle,distance):
        pass
    def setPosition(self,coords):
        self.Image.rect.x = coords[0]
        self.Image.rect.y = coords[1]
