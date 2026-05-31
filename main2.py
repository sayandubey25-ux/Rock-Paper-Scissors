import random
player=int(input("Welcome to Rock Paper Scissors. Enter 1 for rock, 2 for paper or 3 for scissors."))
comp=random.randint(1, 3)
if player==1:
    print("You choose rock")
    if comp==1:
        print("The opponent chose rock")
    elif comp==2:
        print("The opponent chose paper")
    elif comp==3:
        print("The opponent chose scissors")
    
    if player==comp:
        print("It is a tie.")
    elif comp==player+1:
        print("You lose")
    elif comp==1 and player==3:
        print("You lose")
    elif comp+1==player:
        print("You win")
    elif comp==3 and player==1:
        print("You win")
        
elif player==2:
    print("You choose paper")
    if comp==1:
        print("The opponent chose rock")
    elif comp==2:
        print("The opponent chose paper")
    elif comp==3:
        print("The opponent chose scissors")
    
    if player==comp:
        print("It is a tie.")
    elif comp==player+1:
        print("You lose")
    elif comp==1 and player==3:
        print("You lose")
    elif comp+1==player:
        print("You win")
    elif comp==3 and player==1:
        print("You win")
        
elif player==3:
    print("You choose scissors")
    if comp==1:
        print("The opponent chose rock")
    elif comp==2:
        print("The opponent chose paper")
    elif comp==3:
        print("The opponent chose scissors")
    
    if player==comp:
        print("It is a tie.")
    elif comp==player+1:
        print("You lose")
    elif comp==1 and player==3:
        print("You lose")
    elif comp+1==player:
        print("You win")
    elif comp==3 and player==1:
        print("You win")
        
else:
    print("Not a valid choice")
    
'''    
if comp==1:
    print("The opponent chose rock")
elif comp==2:
    print("The opponent chose paper")
elif comp==3:
    print("The opponent chose scissors")
    
if player==comp:
    print("It is a tie.")
elif comp==player+1:
    print("You lose")
elif comp==1 and player==3:
    print("You lose")
elif comp+1==player:
    print("You win")
elif comp==3 and player==1:
    print("You win")
'''