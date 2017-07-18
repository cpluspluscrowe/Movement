class Team():
    def __init__(self,players,color):
        self.Players = players
        self.Color = color
    def AddPlayer(self,player):
        self.Players.append(player)
    def Pass(self,passingPlayer,receivingPlayer,ball):
        passingPlayer.HasBall = False
        receivingPlayer.HasBall = True
        ball.Move(orig,dest)
