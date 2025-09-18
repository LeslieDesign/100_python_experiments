import random
import art
print(art.logo)

def guess_my_number():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    my_number = random.randint(1, 100)

    if difficulty == "easy":
        attempts_left = 10
    else:
        attempts_left = 5

    while attempts_left:
        print(f"You have {attempts_left} chances to guess the number.")
        guess = input("\nMake a guess: ")
        my_guess = int(guess)
        if my_guess == my_number:
            print("You win!")
            break
        elif my_guess > my_number:
            print("Too high.\nGuess again.")
        elif my_guess < my_number:
            print("Too low.\nGuess again.")
        attempts_left -= 1
        if attempts_left == 0:
            print("You're out of chances!")

    print(f"The number was: {my_number}")


guess_my_number()