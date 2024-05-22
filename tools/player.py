class player:
    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, score=0, pos=0):
        self.name = name    #player name
        self.score = 0      #Score tracker
        self.pos = 0        #position
        self.Apos = 0       #animate position

def make_player(name):
    player = player(name)
    return player