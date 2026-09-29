player_score=0
computer_score=0
import random

while True:
     player=input("what is your move ?? rock, paper, or scissors.")
     computer=random.choice(["rock","paper","scissor"])
     print("computer move is" , computer)
    
     if player==computer:
                print("match drawn / both will get a point")
                player_score = player_score + 1
                computer_score = computer_score + 1
     elif player=="rock" and computer=="paper" or player=="scissor" and computer=="rock" or player=="paper" and computer=="scissor":
                    print(" computer wins")
                    computer_score = computer_score + 1
     elif player=="paper" and computer=="rock" or  player=="scissor" and computer=="paper" or player=="rock" and computer=="scissor":
                print(" player wins")
                player_score = player_score + 1
     else:
                print(" please chosee a valid move  !!")
     if player_score==3:
                print(" player wins the game !!")
                break
     elif computer_score==3:
                print(" computer wins the game  !!")
                break