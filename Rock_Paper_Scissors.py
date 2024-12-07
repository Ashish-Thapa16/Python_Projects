import random

def rps() :
    choices = ["Rock", "Paper", "Scissors"]
    while True :
        user = input("Rock/Paper/Scissors? Choose by typing (r/p/s): ").lower()
        if user not in ["r", "p", "s"] :
            print("Invalid Choice!")
            continue
        if user == "r" :
            user_choice = "Rock"
        elif user == "p" :
            user_choice = "Paper"
        elif user == "s" :
            user_choice = "Scissors"

        computer_choice = random.choice(choices)

        print(f"You chose {user_choice} and the Computer chose {computer_choice}")

        if user_choice == computer_choice :
            print("Its a draw! You both chose the same.")

        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper") :
            print("Congratulations! You won!") 

        else :
            print("Sorry, you lost! Better luck next time.")

        user1 = input("Would you like to continue? (y/n): ").lower()
        
        if user1 != "y" :
            print("Thanks for playing. Goodbye!")
            break
rps()   
