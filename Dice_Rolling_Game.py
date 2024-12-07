import random
import time

def rollingDice() :
    while True :
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        user = input("Do you want to roll the dice? (y/n): ").lower()
        if user == "y" :
            print("Rolling...")
            time.sleep(1)
            print((dice1, dice2))
        elif user == "n" :
            print("Thanks for playing!")
            break
        else :
            print("Invalid Choice")

rollingDice()