import pygame
from pygame.locals import *
import time
from tools.actions import *  # actions
from tools.board import *  # returns XY coordinates for board
from tools.cardDeck import *
from tools.dice import *  # for different dice type
from tools.player import *  # make player an object

# to do
# make goomba stomp image and move piece back only after other piece moves on it
# delay input until animation complete
# display game info on the game board
# change number system for cards to use two digit for more card options 01,02,03 ect
# enable  actions for card choices

gameDeck = makeD()  # read in the Card.txt file to make cards
# printD(gameDeck)    # test cards
gSize = 40  # game board size move this in to board handler?
turn = 0  # what players turn
PlayerCount = 2  # number of players
ActivePlayer = 0  # Used for player turn tracking
NextPlayer = 1  # temp for beta
gameController = 0  # 0:Board 1:Animate 2:Card

# Make Players
Players = []  # list to store player
for i in range(0, PlayerCount):
    TempObject = player(i)  # create player
    Players.append(TempObject)  # store player

# Make and set default names to players
colorNames = ['RED', 'BLUE', 'PINK', 'YELLOW', 'GREEN', 'BLACK']
count = 0
for obj in Players:
    obj.name = colorNames[count]
    count = count + 1

# Make game window
pygame.init()
screen = pygame.display.set_mode([550, 550])  # Window size
pygame.display.set_caption('IZY2091 Pygame')  # window name

Black = (0, 0, 0)  # preset color for text
White = (255, 255, 255)
Gray = (125, 125, 125)
largeFont = pygame.font.SysFont(None, 50)  # preset default font
smallFont = pygame.font.SysFont(None, 25)  # preset default font

button1 = pygame.Rect(75, 350, 375, 48)
button2 = pygame.Rect(75, 400, 375, 48)
button3 = pygame.Rect(75, 450, 375, 48)
button4 = pygame.Rect(75, 500, 375, 48)

# load images
background = pygame.image.load('images/Game_b2.png').convert_alpha()
red = pygame.image.load("images/RED.png").convert_alpha()
blue = pygame.image.load("images/BLUE.png").convert_alpha()
cardFrame = pygame.image.load("images/CARD.png").convert()
cardPic = pygame.image.load("art/ERROR.png").convert()

card = False  # detect when card is active
running = True  # trigger game close
while running:

    # Get user input
    for event in pygame.event.get():
        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False

        # if mouse event and card clicked
        elif event.type == MOUSEBUTTONDOWN:
            if card:
                if button1.collidepoint(event.pos):
                    if len(gameDeck[cardDraw].choicesText) == 0:
                        print("Button 0 clicked!")  # do nothing
                    else:
                        print(actions(Players, ActivePlayer, gameDeck[cardDraw].choicesPower[0]))
                        print("Button 1 clicked!")
                        print(gameDeck[cardDraw].choicesPower[0])
                    card = False
                elif button2.collidepoint(event.pos) and len(gameDeck[cardDraw].choicesText) >= 2:
                    print(actions(Players, ActivePlayer, gameDeck[cardDraw].choicesPower[1]))
                    print("Button 2 clicked!")
                    card = False
                elif button3.collidepoint(event.pos) and len(gameDeck[cardDraw].choicesText) >= 3:
                    print(actions(Players, ActivePlayer, gameDeck[cardDraw].choicesPower[2]))
                    print("Button 3 clicked!")
                    card = False
                elif button4.collidepoint(event.pos) and len(gameDeck[cardDraw].choicesText) >= 4:
                    print(actions(Players, ActivePlayer, gameDeck[cardDraw].choicesPower[3]))
                    print("Button 4 clicked!")
                    card = False
                else:
                    print("Invalid Click")
                gameController = 1

        # input logic
        elif (event.type == pygame.KEYDOWN) and (gameController == 0):
            if event.key == pygame.K_c:  # card test <<<<<< REMOVE
                if card:
                    card = False
                else:
                    card = True
                    cardDraw = drawCard(gameDeck)
                    printC(gameDeck[cardDraw])
                    cardArt = gameDeck[cardDraw].image
                    cardPic = pygame.image.load(cardArt).convert_alpha()
                    cardText = gameDeck[cardDraw].text
                    gameController == 1

            if event.key == pygame.K_w:  # take turn
                gameController = 1  # set to animation
                turn = turn + 1
                ActivePlayer = NextPlayer  # change active and next player
                NextPlayer = NextPlayer + 1
                if ActivePlayer == PlayerCount:  # prevent overflow
                    ActivePlayer = 0
                if NextPlayer == PlayerCount:  # prevent overflow
                    NextPlayer = 0
                diceRoll = d6()
                print(Players[ActivePlayer].name, 'rolled a', diceRoll)
                Players[ActivePlayer].pos = Players[ActivePlayer].pos + diceRoll  # roll dice
                if Players[ActivePlayer].pos >= gSize:  # if out of range subtract board and +1 score
                    Players[ActivePlayer].pos = Players[ActivePlayer].pos - gSize
                    Players[ActivePlayer].score = Players[ActivePlayer].score + 1

                for obj in Players:  # if land on same spot goomba stomp
                    if obj.pos == Players[ActivePlayer].pos:
                        if obj != Players[ActivePlayer]:
                            obj.pos = 0
                            obj.Apos = 0
                            print("Goomba Stomp")

            # for game test reasons leave like this for now remove later
            elif event.key == pygame.K_r:
                ActivePlayer = 0
                NextPlayer = 1
                Players[0].pos = Players[0].pos + 1
                gameController = 1
            elif event.key == pygame.K_b:
                ActivePlayer = 1
                NextPlayer = 0
                Players[1].pos = Players[1].pos + 1
                gameController = 1
        # WIP display for game board
        if event.type == pygame.KEYDOWN:  # print once per key press
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Blue score: ", Players[1].score)
            print("Red  score: ", Players[0].score)
            print("Pygame Turn", turn)
            print("Blue POS", Players[1].pos)
            print("Red  POS", Players[0].pos)

    if gameController == 1:  # animation
        done = True
        for obj in Players:
            # test for out of range
            if obj.pos >= gSize:
                obj.pos = obj.pos - gSize
            elif obj.pos < 0:
                obj.pos = obj.pos + gSize
            if obj.Apos != obj.pos:
                obj.Apos = obj.Apos + .125
                time.sleep(.016)
                if obj.Apos >= gSize:
                    obj.Apos = obj.Apos - gSize
                done = False

        if done:
            # test for goomba stomp here
            for obj in Players:
                if obj.pos == Players[ActivePlayer].pos and obj != Players[ActivePlayer]:
                    if Players[ActivePlayer].pos != 0:  # Breaking up if statement for word wrap
                        obj.pos = 0
                        obj.Apos = 0
                        print("Goomba Stomp")  # Make this an image later
            gameController = 0  # switch to game board if animation is done

    # Update Scoreboard text
    line1 = 'P1: ' + Players[0].name + ' Score: ' + str(Players[0].score)
    line2 = 'P2: ' + Players[1].name + ' Score: ' + str(Players[1].score)
    if Players[ActivePlayer].pos == Players[ActivePlayer].Apos:
        line3 = 'Player: ' + Players[NextPlayer].name
    else:
        line3 = 'Player: ' + Players[ActivePlayer].name

    text_line1 = largeFont.render(line1, True, Black)
    text_line2 = largeFont.render(line2, True, Black)
    text_line3 = largeFont.render(line3, True, Black)
    place_line1 = text_line1.get_rect(topleft=(50, 50))
    place_line2 = text_line2.get_rect(topleft=(50, 100))
    place_line3 = text_line3.get_rect(topleft=(50, 150))

    # Draw screen
    screen.fill(Gray)  # background
    screen.blit(background, (0, 0))  # print game board
    screen.blit(text_line1, place_line1)
    screen.blit(text_line2, place_line2)
    screen.blit(text_line3, place_line3)
    screen.blit(red, (boardX(Players[0].Apos), boardY(Players[0].Apos)))  # print Red player
    screen.blit(blue, (boardX(Players[1].Apos), boardY(Players[1].Apos)))  # print Blue player

    if card:  # Display card if 'card' is true
        screen.blit(cardFrame, (50, 50))
        screen.blit(cardPic, (85, 110))

        cardTitle = gameDeck[cardDraw].title  # Button text
        cardTitle = smallFont.render(cardTitle, True, Black)  # color and font
        place_cardTitle = cardTitle.get_rect(topleft=(150, 75))  # placement
        screen.blit(cardTitle, place_cardTitle)

        if len(gameDeck[cardDraw].choicesText) == 0:
            # print('No Options')
            button = pygame.Rect(75, 350, 375, 48)
            pygame.draw.rect(screen, 0, button)
            # Button text
            buttonLine = 'OK'  # Button text
            text_buttonLine = largeFont.render(buttonLine, True, White)  # color and font
            place_text_buttonLine = text_buttonLine.get_rect(topleft=(75, 350))  # placement
            screen.blit(text_buttonLine, place_text_buttonLine)

        # reset cardY
        cardY = 350
        choices = len(gameDeck[cardDraw].choicesText)
        if choices > 4:
            choices = 4
        for i in range(0, choices):
            # Button background
            button = pygame.Rect(75, cardY, 375, 48)
            pygame.draw.rect(screen, 0, button)
            # Button text
            # print(cardPower(gameDeck[cardDraw],i))
            buttonLine = cardPower(gameDeck[cardDraw], i)
            text_buttonLine = smallFont.render(buttonLine, True, White)  # color and font
            place_text_buttonLine = text_buttonLine.get_rect(topleft=(75, cardY))  # placement
            screen.blit(text_buttonLine, place_text_buttonLine)
            cardY = cardY + 50

    pygame.display.update()
pygame.quit()
