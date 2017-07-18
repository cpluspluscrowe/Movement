class Match():
    def __init__(self,team1,team2):
        self.Team1 = team1
        self.Team2 = team2
        self.AllPlayers = team1.Players + team2.Players #append lists together
