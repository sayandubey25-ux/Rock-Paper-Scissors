'''
player_choice=input
comp_choice=random

state what player and computer has chosen

if player_choice==comp_choice:
    tie
(all losing conditions)    
elif player_choice==1 and comp_choice==2:
    you lose
elif player_choice==2 and comp_choice==3:
    You lose
elif player_choice==3 and comp_choice==1:
    you lose
(all winning conditions)
elif player_choice==1 and comp_choice==3:
    you win
elif player_choice==2 and comp_choice==1:
    you win
elif player_choice==3 and comp_choice==2:
    you win


print results
'''
import random
player_choice=int(input("1 for rock, 2 for scissors, 3 for paper. "))
comp_choice=random.randint(1, 3)
if player_choice==comp_choice:
    print("It is a tie.") 
elif player_choice==1 and comp_choice==2:
    print("You chose Rock, Computer chose Paper. You lose")
elif player_choice==2 and comp_choice==3:
    print("You chose Paper, Computer chose Scissors. You lose")
elif player_choice==3 and comp_choice==1:
    print("You chose Scissors, Computer chose Rock. You lose")
elif player_choice==1 and comp_choice==3:
    print("You chose Rock, Computer chose Scissors. You Win")
elif player_choice==2 and comp_choice==1:
    print("You chose Paper, Computer chose Scissors. You win")
elif player_choice==3 and comp_choice==2:
    print("You chose Scissors, Computer chose Paper. You win")
else:
    print("Not a valid choice.")





