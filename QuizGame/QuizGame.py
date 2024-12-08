import json

with open("quiz.json", "r") as file :
    quiz_data = json.load(file)

score = 0
x = 1
print("Welcome to our quiz game! You can quit at any time by simply typing 'Q'.")

for data in quiz_data :
    question = data.get("question")
    option_A = data.get("A")
    option_B = data.get("B")
    option_C = data.get("C")
    option_D = data.get("D")
    answer = data.get("answer")

    print(f"Q{x}). {question}")
    x += 1
    print(f"A: {option_A}")
    print(f"B: {option_B}")
    print(f"C: {option_C}")
    print(f"D: {option_D}")

    user_ans = input("Please enter your answer by choosing A, B, C, or D: ").upper()

    if user_ans == answer :
        print("Great job! Your answer is correct.")
        score += 1
    elif user_ans == "Q" :
        print(f"Thank you for playing! Your total score is {score}")
        break
    else :
        print(f"Oops! That's not quite right. The correct answer is {answer}")

    print(f"Your current score is {score}")
        