import os
# Written this way for fast user readability
CardPower = []
CardPower.append('0 Random option')
CardPower.append('1 Moved player forward 3 spaces')
CardPower.append('2 Moved player forward by dice roll')
CardPower.append('3 All players moved up 3 spaces')
CardPower.append('4 All players move up dice roll')
CardPower.append('5 All players move back 3 spaces')
CardPower.append('6 Move player to random spot')
CardPower.append('7 All players move to random spot ')
CardPower.append('8 All players back to start ')
CardPower.append('9 Do Nothing')


class Card:
    def __init__(self, title, image, text):
        self.title = title
        self.image = image
        self.text = text
        self.choicesPower = []
        self.choicesText = []


def printC(card):
    print('Name:  ', card.title)
    print('Image: ', card.image)
    print('Text:  ', card.text)
    print('Choices:', len(card.choicesText))
    for i in range(len(card.choicesPower)):
        print('  ', cardPower(card, i))
    return f''

def cardPower(card,int):
    if card.choicesText[int] == 'No Text':  # if not custom text use default
        return(CardPower[card.choicesPower[int]][2:])
    else:  # Print text
        return(card.choicesText[int][:-1])

# deck obj
class Deck:
    def __init__(self):
        self.cards = []


def printD(deck):  # print deck
    print('~~~')
    for cards in deck:
        printC(cards)
        print('~~~')
    return r''


def makeD():  # deck builder
    deck = []  # to hold imported cards
    x = 0  # to track each card line number
    #with (open("../Text.txt") as text):  # Read cards from .txt file (For user mods)
    with (open("Cards.txt")as text):  # Read cards from .txt file (For user mods)
        for line in text:
            if line.strip().startswith("#"):  # Skip lines starting with "#" for .txt comments
                pass
            else:
                x = x + 1
                textLine = line.strip()
                if (x < 3) and (line.strip() == ''):    # dont save incomplete cards
                    x = 0
                elif x == 1:
                    title_1 = line.strip()
                elif x == 2:
                    if os.path.exists('art/' + line.strip() + '.png'):  # Check if file is valid If not use error file
                        image_2 = 'art/' + line.strip() + '.png'
                    else:
                        image_2 = 'art/ERROR.png'
                elif x == 3:
                    text_3 = line.strip()
                    card0 = Card(title_1, image_2, text_3)
                elif textLine and textLine[0].isdigit():
                    card0.choicesPower.append(int(line[0]))  # if valid int save
                    card0.choicesText.append(line[2:] if len(line) > 2 else 'No Text')
                elif line.strip() == '':
                    deck.append(card0)  # Save created card to deck and prep fpr next card
                    x = 0
    return deck
