player_score=0
computer_score=0
import random


while True:
     guess=input("what is your move ?? rock, paper, or scissors.")
     computer=random.choice(["rock","paper","scissor"])
     print("computer move is" , computer)
    
     if guess==computer:
                print("match draw !! well played __ both gets a point")
                player_score = player_score + 1
                computer_score = computer_score + 1
     elif guess=="rock" and computer=="paper":
                    print(" computer wins")
                    computer_score = computer_score + 1
     elif guess=="paper" and computer=="rock":
                print(" player wins")
                player_score = player_score + 1
     elif  guess=="scissor" and computer=="paper":
                print(" player wins")
                player_score = player_score + 1
     elif guess=="paper" and computer=="scissor":
                print(" computer wins")
                computer_score = computer_score + 1
     elif guess=="scissor" and computer=="rock":
                print(" computer wins")
                computer_score = computer_score + 1
     elif guess=="rock" and computer=="scissor":
                print(" player wins")
                player_score = player_score + 1
     else:
                print(" please chosee a valid move  !!")
     if player_score==3:
                print(" player wins the game / / cogratss!!  !!")
                break
     elif computer_score==3:
                print(" computer wins the game / better luck next time  !!")
                break
