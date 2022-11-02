#Welcome to a game of blackjack made in python3...
import random

class Card:
    def __init__(self):
        self.card = random.randint(2,11)

deck_of_cards = ["2♦","2♥","2♠","2♣","3♦","3♥","3♠","3♣","4♦","4♥","4♠","4♣","5♦","5♥","5♠","5♣","6♦","6♥","6♠","6♣","7♦","7♥","7♠","7♣","8♦","8♥","8♠","8♣","9♦","9♥","9♠","9♣","10♦","10♥","10♠","10♣","Jack♠","Jack♣", "Jack♥", "Jack♦", "Queen♠", "Queen♣", "Queen♥", "Queen♦", "King♦", "King♥", "King♣", "King♠", "Ace♠", "Ace♣", "Ace♥", "Ace♦"]