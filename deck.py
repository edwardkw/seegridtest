# Edward Kwiatkowski, 10/31/2020, for Seegrid Interview
import random

class Card:
  def __init__(self, suit, value):
    self.__suit = suit
    self.__value = value

  def __repr__(self):
    return self.__value + ' of ' + self.__suit

class Deck:
  # defaults to standard deck, can be used for 'special' cards/decks
  def __init__(self, suits=['Clubs','Diamonds','Hearts','Spades'], values=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']):
    self.__size = len(suits)*len(values)
    self.__deck = []
    for suit in suits:
      for value in values:
        self.__deck.append(Card(suit, value))
    self.__place_in_deck = 0
  
  # added optional param 'full' to specify whether all dealt cards are returned to the deck before shuffle
  def shuffle(self, full=False):
    newDeck = []
    if full:
      self.__place_in_deck = 0
    while len(self.__deck):
      if self.__place_in_deck == len(self.__deck) - 1:
        newDeck = self.__deck[0:self.__place_in_deck + 1] + newDeck
        self.__deck = []
      else:
        randomIndex = random.randint(self.__place_in_deck, len(self.__deck) - 1)
        newDeck.append(self.__deck.pop(randomIndex))
    self.__deck = newDeck

  # no card dealt if none left
  def deal_card(self):
    if self.__place_in_deck == self.__size:
      return None
    else:
      self.__place_in_deck += 1
      return self.__deck[self.__place_in_deck - 1]

  def __repr__(self):
    if self.__place_in_deck != self.__size:
      return f'Dealt cards: {self.__deck[:self.__place_in_deck]} \nCards in deck: {self.__deck[self.__place_in_deck:]}'

# some sample usage
sampleDeck = Deck()
print(sampleDeck)
sampleDeck.deal_card()
sampleDeck.deal_card()
sampleDeck.deal_card()
print(sampleDeck)
sampleDeck.shuffle()
print(sampleDeck)
sampleDeck.shuffle(True)
print(sampleDeck)
