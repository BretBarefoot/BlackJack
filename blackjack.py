#Welcome to a game of blackjack made in python3...
import random

deck_of_cards = ["2♦","2♥","2♠","2♣","3♦","3♥","3♠","3♣","4♦","4♥","4♠","4♣","5♦","5♥","5♠","5♣","6♦","6♥","6♠","6♣","7♦","7♥","7♠","7♣","8♦","8♥","8♠","8♣","9♦","9♥","9♠","9♣","10♦","10♥","10♠","10♣","Jack♠","Jack♣", "Jack♥", "Jack♦", "Queen♠", "Queen♣", "Queen♥", "Queen♦", "King♦", "King♥", "King♣", "King♠", "Ace♠", "Ace♣", "Ace♥", "Ace♦"]
card_value = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]
#zip the lists into a diction where the key is the card name and value is card points
deck_dict = {key:value for key, value in (zip(deck_of_cards, card_value))}
drawn_cards = []

class Player:


    def __init__(self,isDealer=True):
        #sets up your personal deck
        self.deck = deck_dict
        dealer_score = 0
        player_score = 0
        

        #pick a random cards from from list of keys, gets the value from the keys, removed the key:value from the dictionary
        self.random_card1 = random.choice(list(self.deck.keys()))
        self.card1 = self.deck.get(self.random_card1)
        deck_dict.pop(self.random_card1)

        self.random_card2 = random.choice(list(self.deck.keys()))
        self.card2 = self.deck.get(self.random_card2)
        deck_dict.pop(self.random_card2)

        #hides a dealer card and shows player cards and score
        if isDealer == True:
            print(self.random_card1)
            print("X")
        else: 
            print(self.random_card1)
            print(self.random_card2) 

        #reassigns the value if the cards jack-king
        if self.card1 > 10 and self.card1 < 14:
            self.card1 = 10
        elif self.card2 > 10 and self.card2 < 14:
            self.card2 = 10
        elif self.card1 == 14:
            self.card1 = 11
        elif self.card2 == 14:
            self.card2 = 11

        #sets either dealer or players score off the deal
        if isDealer == True:
            dealer_score = self.card1 + self.card2
        else:
            player_score = self.card1 + self.card2    

        if player_score > 21 and isDealer == False and card1 == 14:
            card1 = 1
            player_score = self.card1 + self.card2

        elif player_score > 21 and isDealer == False and card2 == 14:
            card2 = 1
            player_score == self.card1 + self.card2


def count_dealer_draw(score1,score2):
    if(score1+score2) > 21 and score1 == 11:
        score1 = 1
        dealer_points = score1 + score2
        return dealer_points
    elif(score1+score2) > 21 and score2 == 11:
        score2 = 1
        dealer_points = score1 + score2
        return dealer_points  
    else:
        return score1 + score2

def count_player_draw(score1,score2):
    if(score1+score2) > 21 and score1 == 11:
        score1 = 1
        player_points = score1 + score2
        return player_points
    elif(score1+score2) > 21 and score2 == 11:
        score2 = 1
        player_points = score1 + score2
        return player_points  
    else:
        return score1 + score2   

def say_phrase(phrase1,phrase2):
    print(phrase1 + phrase2)               




def check_blackjack():        
    if isDealer == True and dealer_score == 21:
        print("Dealer Has BLACKJACK!!  " + self.random_card1 + " " + self.random_card2)    


        #Checks for Player Blackjack on the deal
    if isDealer == False and player_score == 21:
        print("You WIN! BLACKJACK!!!!  " + self.random_card1 + " " + self.random_card2)




  




print("The Dealers Cards are:")   
dealer_cards = Player(isDealer=True)
print("The Players Cards are:")
player_cards = Player(isDealer=False)


p_score = count_player_draw(player_cards.card1, player_cards.card2)
d_score = count_dealer_draw(dealer_cards.card1,dealer_cards.card2)

if d_score == 21:
    print("Dealer Has BlackJack!!   " + dealer_cards.random_card1 + dealer_cards.random_card2)
elif p_score == 21:
    print("You have BlackJack!!!!   " + player_cards.random_card1 + player_cards.random_card2)
elif p_score == 21 and d_score == 21:
    print("You both have BlackJack! It's a Push!")
else:
    print("\nYour Current Score Is " + str(p_score) + "       The Dealer Has: " + str(dealer_cards.card1) + " showing.")
    print("\nRemember the Dealer must hit on 16 and stand on anything over 17.") 
    print("\nDo you want to Hit or Stay?")            







