import random

""" Blackjack set up"""
limit = 21
cards_left = 52
player_cards = 0
dealer_cards = 0
player_score = 0
dealer_score = 0

""" start """
player_cards += random.randint(1,11)
player_cards += random.randint(1,11)
dealer_cards += random.randint(1,11)
dealer_cards += random.randint(1,11)
cards_left -= 4

""" dealer automatic """
while dealer_cards < 17:
    dealer_cards += random.randint(1,11)
    cards_left -= 1

""" hit or stay """
while player_cards < 21:
    print(player_cards)
    choice = input("Hit or stay?")
    if choice == "hit":
        player_cards += random.randint(1,11)
        cards_left -= 1
        continue
    else:
        break
        
""" score """
if player_cards <= 21 and player_cards > dealer_cards:
    player_score += 1
elif dealer_cards < 21 and dealer_cards > player_cards:
    dealer_score += 1
    
    
def main():
    while 1:    
        cards_left = 52     #Standard deck count
        player_cards = 0    #current total for player 
        dealer_cards = 0    #current total for dealer
        player_score = 0    
        dealer_score = 0
        player_cards += random.randint(1,11)    #adds a card/number to current total
        player_cards += random.randint(1,11)
        dealer_cards += random.randint(1,11)
        dealer_cards += random.randint(1,11)
        cards_left -= 4                         #subtracts cards
        
        while cards_left > 0:               #Keeps track of deck.
            while 1:
                if dealer_cards == 21:        #If dealer gets 21 it gets a point
                    print("Dealer: 21")
                    break
                elif dealer_cards < 17:    #Dealers must keep going until they are >= 17
                    dealer_cards += random.randint(1,11)
                    cards_left -= 1
                    continue
                else:
                    break
                   
            while 1:
                if dealer_cards == 21:
                    dealer_score +=1
                    print("Dealer score: " + str(dealer_score) + "\n")
                    print("Player score: " + str(player_score) + "\n")
                    break
                elif dealer_cards > 21:
                    player_score += 1
                    print("Dealer score: " + str(dealer_score) + "\n")
                    print("Player score: " + str(player_score) + "\n")
                    break
                print("Dealer: " + str(dealer_cards))
                print("Player: " + str(player_cards))
                if player_cards < 21:
                    choice = input("Hit or stay? ")
                    if choice == "hit":
                        player_cards += random.randint(1,11)
                        cards_left -= 1
                        if player_cards < 21: 
                            continue
                        elif player_cards > 21:
                            break
                        elif player_cards == 21:
                            break
                    else:
                        break
                else:
                    break   
            if player_cards <= 21 and player_cards > dealer_cards:
                player_score += 1
                print(str(player_score) + "\n")
                continue
            elif dealer_cards < 21 and dealer_cards > player_cards:
                dealer_score += 1
                print(str(dealer_cards) + "\n")
                continue
        if dealer_score > player_score:
            print("Dealer wins.")
        elif player_score > dealer_score:
            print("You win. Congrats")
        else:
            print("Tie. Good game.")
        retry = input("Play again? (y/n) ")
        if retry == "y":
            continue
        else:
            break
    
main()

    
