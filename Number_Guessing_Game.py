import random

def guessNumber() :
    computer = random.randint(1,100)
    while True :
        user = input("Guess a number between 1 and 100: ")
        if not user.isdigit() or int(user) > 100 :
            print("Please enter a valid number")
            continue
        
        user_guess = int(user)
        if user_guess == computer :
            print("Congratulations! You guessed the number right.")
            break
            
        elif user_guess < computer :
            print("Too low!")

        elif user_guess > computer :
            print("Too high!")

guessNumber()