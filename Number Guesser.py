#This is just a simple guessing game where the script randomly generates a number from 1 through 50 and asks the user to guess the number.
import random

username = input(f"Welcome to Number Guesser! Before we begin the game, what should I call you?")

print(f"""\nVery well, {username}.

This script will randomly generate a number from 1 through 10.
The objective of the game is simple: Guess the number correctly.
For each incorrect answer, you will lose a point.
For each correct answer, you will gain FIVE points.

Note that this program can be ended at any time by typing Ctrl+C.
""")

score = 0

while True:
    generated_number = random.randint(1,10)
    while True:
        try:
            user_guess = int((input(f"\nNow, {username}, guess a number from 1 through 10:")))
            if user_guess not in range(1, 11):
                print("Invalid entry! Please enter a valid integer from 1 through 10.")
                continue
            if user_guess < generated_number:
                score += -1
                print(f"\nToo low! Your score is {score}. Guess again.")
            elif user_guess > generated_number:
                score += -1
                print(f"\nToo high! Your score is {score}. Guess again.")
            elif user_guess == generated_number:
                score += 5
                print(f"You guess correctly! Your score is {score}.")
                break
        except ValueError:
            print("Invalid entry! Please enter a valid integer from 1 through 10.")
            continue
        except KeyboardInterrupt:
            print(f"\nExiting game. Goodbye, {username}!")
            break
    restart = input(f"\n{username}, would you like to play the game again? (Yes/No):").strip().lower()
    if restart not in ["yes", "no"]:
        print("Invalid entry! Enter yes or no.")
    elif restart != "yes":
        print(f"Thank you for playing the game! Have a good one, {username}.")
        break
