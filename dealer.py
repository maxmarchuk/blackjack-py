#!/usr/bin/python
from random import shuffle

class Card(object):
    #overload str function to print the class. e.g. Ace of Spades
    def __str__(self):
        return str(self.value) + ' of ' + self.suit

    def __init__(self, suit=None, value=None, rank=None):
        self.suit = suit
        self.value = value
        self.rank = rank

def getDeck():
    deck = [] 
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen']

    for suit in suits:
        for value in values:
            deck.append(Card(suit, value))

    return deck

def getShuffledDeck():
    deck = getDeck()
    shuffle(deck)
    return deck

def valueOf(card):
     
    
def play():
    deck = getShuffledDeck()
    dealerHand = []
    playerHand = []
    
    for a in deck:
        print a

    dealerHand.append(deck.pop)
    print 'Dealer Hand: '
    for card in dealerHand:
        print card

    playerHand.append(deck.pop())
    print 'Your Hand: '  


