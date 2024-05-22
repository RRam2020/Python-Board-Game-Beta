import random

def drawCard(deck):
    num = random.randint(0,len(deck)-1)
    return num

def dice(max):
    num = random.randint(1,max)
    return num

def d6():
    return dice(6)
