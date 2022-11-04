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
            print(self.random_card2)
        else: 
            print(self.random_card1)
            print(self.random_card2) 

        #reassigns the value if the cards jack-king
        if self.card1 > 10 and self.card1 < 14:
            self.card1 = 10
        elif self.card2 > 10 and self.card2 < 14:
            self.card2 = 10

        if self.card1 == 14: #ace
            self.card1 = 11
        elif self.card2 == 14:
            self.card2 = 11

    def draw_card(self):
        self.new_card = random.choice(list(self.deck.keys()))
        self.new_card_points = self.deck.get(self.new_card)
        deck_dict.pop(self.new_card)

        if self.new_card_points > 10 and self.new_card_points < 14: #10-13 jack to king
            self.new_card_points = 10
        elif self.new_card_points == 14:
            self.new_card_points = 11
        return(self.new_card, self.new_card_points)
 


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



def check_blackjack_on_draw(d_score,p_score):        
    if d_score == 21:
        print("Dealer Has BlackJack!!   " + dealer_cards.random_card1 + dealer_cards.random_card2)
        quit()
    elif p_score == 21:
        print("You have BlackJack!!!!   " + player_cards.random_card1 + player_cards.random_card2)
        quit()
    elif p_score == 21 and d_score == 21:
        print("You both have BlackJack! It's a Push!")
        quit()
    else:
        print("\nYour Current Score Is " + str(p_score) + "       The Dealer Has: " + str(dealer_cards.card1) + " showing.")
        print("\nRemember the Dealer must hit on 16 and stand on anything over 17.") 
        print("\nDo you want to Hit or Stay?")  

def get_input():
    player_input = input()
    player_input = player_input.lower()
    return player_input

def check_input(user_input):
    if user_input == "hit":
        card, points = player_cards.draw_card()
        return card,points
        
    elif user_input == "stay":
        return user_input

    else:
        print("\nInvalid Input.    \nType Hit or Stay and press Enter.")
        get_input()

#############################################################################################


print("The Dealers Cards are:\n")   
dealer_cards = Player(isDealer=True)
print("The Players Cards are:\n")
player_cards = Player(isDealer=False)


p_score = count_player_draw(player_cards.card1, player_cards.card2)
d_score = count_dealer_draw(dealer_cards.card1,dealer_cards.card2)

check_blackjack_on_draw(d_score, p_score)

user_input = get_input()
if user_input == "hit":
    card,points = check_input(user_input)
    p_score += points

    if p_score > 21:
        print("\n You Drew: " + card + "  Your Score is: " + str(p_score))
        print("\n\nYou bust! Game Over!")
        quit()

    print("You drew " + card + " Your score is: " + str(p_score))
    print("\nDo you want to Hit or Stay?")  

    user_input2 = get_input()

    if user_input2 == "hit":
        card, points = check_input(user_input2)
        p_score += points
        print("\nYou drew " + card + " Your score is: " + str(p_score))

        if p_score > 21:
            print("\n\nYou bust! Game Over!")
            quit()


        user_input3 = get_input()

        if user_input3 == "hit":
            card,points = check_input(user_input3)
            p_score += points
            print("\nYou drew " + card + " Your score is: " + str(p_score))
            if p_score > 21:
                print("\n\nYou bust! Game Over!")
                quit()
            elif p_score <= 21:
                print("\n\nYou got 5 cards! You WIN!")
                quit()    

elif user_input == "stay":
    print("\nYour Score is: " + str(p_score) + "   The Dealer's Score is: " + str(d_score))

    if d_score > 16 and d_score > p_score:
            print("\nDealer Score is:  " + str(d_score) + " The Dealer Stands!")
            print("         The Dealer Wins!!!        ")
            quit()
    elif d_score > 16 and d_score < p_score:
            print("\nDealer Score is:  " + str(d_score) + " The Dealer Stands!")
            print("         The Player Wins!!!        ")
            quit()                   
    elif d_score < 17:
            dcard,dpoints = dealer_cards.draw_card()
            d_score = d_score + dpoints
            print("The Dealer Drew: " + dcard + "     Dealer Score is now:  " + str(d_score))
            if d_score > p_score:
                print("\nDealer Score is:  " + str(d_score) + " The Dealer Stands!")
                print("         The Dealer Wins!!!        ")
                quit()
                
            elif d_score < 17:
                dcard,dpoints = dealer_cards.draw_card()
                d_score = d_score + dpoints
                print("The Dealer Drew: " + dcard + "     Dealer Score is now:  " + str(d_score))

                if d_score > p_score:
                    print("\nDealer Score is:  " + str(d_score) + " The Dealer Stands!")
                    print("         The Dealer Wins!!!        ")
                    quit()


                if d_score < 17:
                    dcard,dpoints = dealer_cards.draw_card()
                    d_score = d_score + dpoints
                    print("The Dealer Drew: " + dcard + "Dealer Has 5 Cards!" + "\n     The Dealer Wins!")               
   
quit()
    












