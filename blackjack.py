#Welcome to a game of blackjack made in python3...my first project in 20 years..first python project
import random
import time

deck_of_cards = ["2♦","2♥","2♠","2♣","3♦","3♥","3♠","3♣","4♦","4♥","4♠","4♣","5♦","5♥","5♠","5♣","6♦","6♥","6♠","6♣","7♦","7♥","7♠","7♣","8♦","8♥","8♠","8♣","9♦","9♥","9♠","9♣","10♦","10♥","10♠","10♣","Jack♠","Jack♣", "Jack♥", "Jack♦", "Queen♠", "Queen♣", "Queen♥", "Queen♦", "King♦", "King♥", "King♣", "King♠", "Ace♠", "Ace♣", "Ace♥", "Ace♦"]
card_value = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
#zip the lists into a diction where the key is the card name and value is card points
deck_dict = {key:value for key, value in (zip(deck_of_cards, card_value))}
fresh_deck = deck_dict
#player_total = 0
#dealer_total = 0
new_card = 0

new_card2 = 0

class Player:


    def __init__(self,isDealer=True):
        #sets up your personal deck
        self.deck = deck_dict
        self.dealer_total = 0
        self.player_total = 0
        #pick a random cards from from list of keys, gets the value from the keys, removed the key:value from the dictionary
        self.random_card1 = random.choice(list(self.deck.keys()))
        self.card1 = self.deck.get(self.random_card1)
        deck_dict.pop(self.random_card1)

        self.random_card2 = random.choice(list(self.deck.keys()))
        self.card2 = self.deck.get(self.random_card2)
        deck_dict.pop(self.random_card2)

        if isDealer == True:
            self.dealer_total = self.card1 + self.card2
        else:
            self.player_total = self.card1 + self.card2    

        #hides a dealer card and shows player cards and score
        if isDealer == True:
            print(self.random_card1,end=""); time.sleep(1); print("      HIDDEN\n");time.sleep(1)

        else: 
            print(self.random_card1,end=""); time.sleep(1); print("         " + self.random_card2);time.sleep(1)



    def player_draw_card(self):
        
        

        self.new_card2 = random.choice(list(self.deck.keys()))
        self.new_card_points = self.deck.get(self.new_card2)
        deck_dict.pop(self.new_card2)

        if self.player_total + self.new_card_points > 21 and self.new_card_points == 11:
            self.new_card_points = 1
            self.player_total += self.new_card_points
        else:    
            self.player_total += self.new_card_points




        time.sleep(2)

        
        print("You Drew: " + self.new_card2 + "       Your points are: " + str(self.player_total))
        print()       

        if self.player_total < 21:
            time.sleep(.5)
            print("Would you like to hit or stay?\n")
            get_input_hit_stay()
        elif self.player_total > 21:
            time.sleep(.5)
            print("\nPlayer Bust..")
            time.sleep(.5)

        elif self.player_total == 21:
            time.sleep(.5)
            print("You have 21! Passing To Dealer...\n")
            dealer_cards.dealer_draw_cards()

        return self.new_card2, self.new_card_points, self.player_total


         



    def dealer_draw_cards(self):
        print("The Dealers Hidden Card is " + self.random_card2 + "      The Dealers Score is: " + str(self.dealer_total))


        time.sleep(1)
        if self.dealer_total >= 17 and self.dealer_total < 22:
            check_scores(self.dealer_total, player_cards.player_total)
        elif self.dealer_total > 21:
            print("The Dealer Bust! You Win!")
            time.sleep(2)    
        else:

            print("\nThe Dealer draws a card")
            time.sleep(2)
            self.new_card2 = random.choice(list(self.deck.keys()))
            self.new_card_points = self.deck.get(self.new_card2)
            deck_dict.pop(self.new_card2)
            if (self.dealer_total + self.new_card_points) > 21 and self.new_card_points == 11:
                self.new_card_points = 1
            else:
                print("\nThe Dealer Drew: " + self.new_card2)
                self.dealer_total = self.new_card_points + self.dealer_total
                time.sleep(2)
                print("\nThe Dealers Score is " + str(self.dealer_total))

            if self.dealer_total >= 17 and self.dealer_total < 22:
                check_scores(self.dealer_total, player_cards.player_total)
            elif self.dealer_total > 21:
                print("The Dealer Bust! You Win!")
                time.sleep(1)
                pass  
            else:
                print("\nThe Dealer draws a card")
                time.sleep(1)
                self.new_card2 = random.choice(list(self.deck.keys()))
                self.new_card_points = self.deck.get(self.new_card2)
                deck_dict.pop(self.new_card2)
                
                if (self.dealer_total + self.new_card_points) > 21 and self.new_card_points == 11:
                    self.new_card_points = 1
 
                
                print("\nThe Dealer Drew: " + self.new_card2)
                time.sleep(1)
                self.dealer_total = self.new_card_points + self.dealer_total
                print("\nThe Dealers Score is " + str(self.dealer_total)) 
                if self.dealer_total >= 17 and self.dealer_total < 22:
                    check_scores(self.dealer_total, player_cards.player_total)
                elif self.dealer_total > 21:
                    time.sleep(1)
                    print("The Dealer Bust! You Win!")
                    pass  
                else:
                    print("\nThe Dealer draws a card")
                    time.sleep(1)
                    self.new_card2 = random.choice(list(self.deck.keys()))
                    self.new_card_points = self.deck.get(self.new_card2)
                    deck_dict.pop(self.new_card2)
                    if (self.dealer_total + self.new_card_points) > 21 and self.new_card_points == 11:
                        self.new_card_points = 1
                    
                    print("\nThe Dealer Drew: " + self.new_card2)
                    time.sleep(1)
                    self.dealer_total = self.new_card_points + self.dealer_total
                    print("\nThe Dealers Score is " + str(self.dealer_total))

                    if self.dealer_total <= 21:
                        print("Dealer has 5 cards and wins automatically!")
                        pass                     

def add_to_player_total(old_total, new_card):
    new_total = old_total + new_card
    return new_total           
             
def count_dealer_draw(score1,score2,new_card):
    if(score1+score2) > 21 and score1 == 11:
        score1 = 1
        dealer_points = score1 + score2
        return dealer_points
    elif(score1+score2) > 21 and score2 == 11:
        score2 = 1
        dealer_points = score1 + score2
        return dealer_points
    elif(score1+score2+new_card) > 21 and new_card == 11:
        new_card = 1
        dealer_points = score1 + score2 + new_card
        return dealer_points
    elif(score1+score2+new_card) > 21 and score1 == 11:
        score1 = 1
        dealer_points = score1 + score2 + new_card
        return dealer_points
    elif(score1+score2+new_card) > 21 and score2 == 11:
        score2 = 1
        dealer_points = score1 + score2 + new_card
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
   


def check_scores(dealer_total, player_total):
    if player_total > dealer_total:
        print("You win!")
        time.sleep(1)

    elif dealer_total > player_total:
        print("Dealer Wins")
        time.sleep(1)

    else:
        print("It was a push!")
        time.sleep(1)        


def check_blackjack_on_draw():        
    if dealer_cards.dealer_total == 21:
        time.sleep(1)
        print("\nDealer Has BlackJack!!        " + dealer_cards.random_card1 + dealer_cards.random_card2 + "\n")
        return 1 #dealer win

    elif player_cards.player_total == 21:
        time.sleep(1)
        print("\nYou have BlackJack!!!!        " + player_cards.random_card1 + player_cards.random_card2 + "\n")
        return 2 #player win
  
    elif player_cards.player_total == 21 and dealer_cards.dealer_total == 21:
        time.sleep(1)
        print()
        print("\nYou both have BlackJack! It's a Push!\n")
        print()
        return 3 #push

    else:
        print("\nYour Current Score Is " + str(player_cards.player_total) + "       The Dealer Has: " + str(dealer_cards.card1) + " showing.")
        time.sleep(1)
        print("\nRemember the Dealer must hit on 16 and stand on anything over 17.") 
        time.sleep(1)
        print("Do you want to Hit or Stay? Or Type Quit to stop playing.\n") 


def get_input_hit_stay():
    player_input = input()
    player_input = player_input.lower()
    if player_input == "quit":
        quit()
    check_input(player_input)


def check_input(user_input,isDealer=True):
    if user_input == "hit":
        print()
        card, points, newtotal = player_cards.player_draw_card()
        return card,points,user_input

    elif user_input == "stay":
        print("\nThe Player Stood at " + str(player_cards.player_total))
        print()
        time.sleep(1)
        dealer_cards.dealer_draw_cards()
        return user_input
    elif player_cards.player_total == 21:
        print("You have 21 Points! Passing to dealer!\n")
        dealer_cards.dealer_draw_cards()
        time.sleep(1)    

    else:
        print("Invalid Input.Type Hit or Stay or Quit and Press Enter.\n")
        get_input_hit_stay()

    return user_input
#############################################################################################
while True:

    print("-----------------NEW HAND---------------------")
    time.sleep(.5)
    print("The Dealers Cards are:") 
    time.sleep(.5)  
    dealer_cards = Player(isDealer=True)
    time.sleep(.5)
    print("The Players Cards are:")
    time.sleep(.5)
    player_cards = Player(isDealer=False)


    player_cards.player_total = count_player_draw(player_cards.card1, player_cards.card2)
    dealer_cards.dealer_total = count_dealer_draw(dealer_cards.card1,dealer_cards.card2, new_card)

    status = check_blackjack_on_draw()

    if status == 1 or status ==2 or status == 3:
        continue

    user_input = get_input_hit_stay()



    print("\nShuffling Cards\n")
    time.sleep(1)    
    deck_dict = fresh_deck    
        