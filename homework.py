import random
lot_num=random.randint(1, 100)
user_num=int(input("Welcome to the lottery, please enter a number between 1 to 100."))
if user_num==lot_num:
    print("Congratulations! You have won the lottery!")
else:
    print("Better luck next time.")