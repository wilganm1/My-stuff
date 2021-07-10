#Have the computer pick random rock, paper or scissors
#Have it restart when it's over
import random

comp_score = 0
player_score = 0
goal = int(input("Play first to: "))

while True: 
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = str(input("Pick: "))
    print("You picked " + player + "." + " The computer picked " + computer + ".")
    if player == 'rock' and computer == 'scissors' or player == 'paper' and computer == 'rock' or player == 'scissors' and computer == 'paper':
        print("You win!")
        player_score += int(1)
        print("Player score: " + str(player_score))
        print("Computer score: " +  str(comp_score))
    elif player == computer:
        print("Tie!")
        print("Player score: " + str(player_score) )
        print("Computer score: " +  str(comp_score))
    else:
        print("Computer wins!")
        comp_score += int(1)
        print("Player score: " + str(player_score) )
        print("Computer score: " +  str(comp_score))
    
    if player_score == goal:
        print("You are the winner!")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "y":
            comp_score = 0
            player_score = 0
            continue
        else:
            print("Thanks for playing")
            break
            
    elif comp_score == goal:
        print("Computer is the winner!")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "y":
            comp_score = 0
            player_score = 0
            continue
        else:
            print("Thanks for playing")
            break
            
            
