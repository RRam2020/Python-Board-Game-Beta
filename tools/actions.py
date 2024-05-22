# Card powers
# 0 Random option
# 1 Moved player forward 3 spaces
# 2 Move player forward by dice roll
# 3 All players moved up 3 spaces
# 4 All players move up dice roll
# 5 All players move back 3 spaces
# 6 Move player to random spot
# 7 All players move to random spot
# 8 All players back to start
# 9 Do Nothing
from tools.dice import *            # for difrent dice type
from tools.player import *


def actionCard(players,ActivePlayer,action):
    actionCard(players, ActivePlayer, action)
    for player in players:
        player.Apos = player.pos
    return f"action completed"

def actions(players,ActivePlayer,action):
    match action:
        case 0:                                     # call self and pick random option
            action = dice(9)                        # roll for random action
            actions(players,ActivePlayer,action)    # call self with random int
            #return f"0 Random option"
        case 1:
            players[ActivePlayer].pos = players[ActivePlayer].pos+3
            #return f"1 Moved player forward 3 space"
        case 2:
            players[ActivePlayer].pos = players[ActivePlayer].pos + dice(6)
            #return f"2 Move player forward by dice roll"
        case 3:
            for player in players:
                player.pos = player.pos + 3
            #return f"3 All players moved up 3 spaces"
        case 4:
            roll = dice(6)
            for player in players:
                player.pos = player.pos + roll
            #return f"4 All players moved up by dice roll"
        case 5:
            for player in players:          # has a bug if goes past 0
                player.pos = player.pos - 3
                player.Apos = player.pos
            #return f"5 All players move back 3 spaces"
        case 6:
            players[ActivePlayer].pos = dice(41)
            players[ActivePlayer].Apos = players[ActivePlayer].pos
            #return f"6 Move player to random spot"
        case 7:
            for player in players:
                player.pos = dice(41)           # 41 because dice dosen't include 0
                player.Apos = player.pos
            #return f"7 All players move to random spot"
        case 8:
            for player in players:
                player.pos = 0
                player.Apos = player.pos
            #return f"8 All players back to start"
        case 9:
            return f"9 Do Nothing"
            #case _:
            #    return f"Something's wrong with the internet"
    # skip animation
    for obj in players:
        if obj.pos >= 40:
            obj.pos=obj.pos40
        elif 0 > obj.pos:
            obj.pos=obj.pos+40

        obj.Apos = obj.pos
        print('Animate skip')
    return f""
