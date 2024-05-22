# board size hard coded for now
px=50           # px per square

def boardX(pos):
    posx = pos
    if pos < 10:
        x = pos
    elif  pos >= 10 and pos <20:
        x = 10
    elif  pos >= 20 and pos < 30:
        x=30-posx
    elif  pos >= 30 and pos < 40:
        x=0
    elif pos >= 40:
        return boardX(pos-40)
    else:
        x=5
        
    return x*50

def boardY(pos):
    posy = pos
    if pos < 10:
        y = 0
    elif  pos >= 10 and pos <20:
        y = pos - 10
    elif  pos >= 20 and pos < 30:
        y=10
    elif  pos >= 30 and pos < 40:
        y=40- pos
    elif pos >= 40:
        return boardY(pos-40)
    else:
        y=5
    return y*50
