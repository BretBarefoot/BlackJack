#Welcome to a game of blackjack made in python3...
import random

deck_of_cards = ["2♦","2♥","2♠","2♣","3♦","3♥","3♠","3♣","4♦","4♥","4♠","4♣","5♦","5♥","5♠","5♣","6♦","6♥","6♠","6♣","7♦","7♥","7♠","7♣","8♦","8♥","8♠","8♣","9♦","9♥","9♠","9♣","10♦","10♥","10♠","10♣","Jack♠","Jack♣", "Jack♥", "Jack♦", "Queen♠", "Queen♣", "Queen♥", "Queen♦", "King♦", "King♥", "King♣", "King♠", "Ace♠", "Ace♣", "Ace♥", "Ace♦"]
card_value = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]
#zip the lists into a diction where the key is the card name and value is card points
deck_dict = {key:value for key, value in (zip(deck_of_cards, card_value))}
drawn_cards = []



class DrawCards:

    def __init__(self,isDealer=True):
        #sets up your personal deck
        self.deck = deck_dict
     
        
        #pick a random cards from from list of keys

        self.random_card1 = random.choice(list(self.deck.keys()))
        card1 = self.deck.get(self.random_card1)
        deck_dict.pop(self.random_card1)

        self.random_card2 = random.choice(list(self.deck.keys()))
        card2 = self.deck.get(self.random_card2)
        deck_dict.pop(self.random_card2)


        #sets the point values of the cards
        
        
        

        if card1 > 10:
            card1 = 10
        elif card2 > 10:
            card2 = 10    


        if isDealer == True:
            print(self.random_card1)
            print("X")
        else: 
            print(self.random_card1)
            print(self.random_card2)    

        total = card1 + card2
        print(total)
     


   


print("The Dealers Cards are:")   
dealer_cards =DrawCards(isDealer=True)
print("The Players Cards are:")
player_cards =DrawCards(isDealer=False)

