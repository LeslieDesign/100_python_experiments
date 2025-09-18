import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock, paper, scissors]
user_choice = input("What do you choose? Rock (R), Paper (P), Scissors (S): ").lower()
computer_choice = random.randint(0, 2)

if user_choice == "r":
    user_choice = 0
elif user_choice == "p":
    user_choice = 1
elif user_choice == "s":
    user_choice = 2
else:
    print("You entered a letter that's not in my list. Start over!")

print(rock_paper_scissors[user_choice])
# print(user_choice)
print(rock_paper_scissors[computer_choice])
# print(computer_choice)

game_choices = [user_choice, computer_choice]
# print(game_choices)


if game_choices == [0, 2]:  # rock > scissor
    print("Rock crushes Scissors - PLAYER WINS!")

elif game_choices == [2, 1]:     # scissor > paper
    print("Scissors cut Paper - PLAYER WINS!")

elif game_choices == [1, 0]:     # paper > rock
    print("Paper covers Rock - PLAYER WINS!")

elif game_choices == [2, 0]:  # rock > scissor
    print("Rock crushes Scissors - COMPUTER WINS!")

elif game_choices == [1, 2]:  # scissor > paper
    print("Scissors cut Paper - COMPUTER WINS!")

elif game_choices == [0, 1]:  # paper > rock
    print("Paper covers Rock - COMPUTER WINS!")

elif user_choice == computer_choice:
    print("TIE ANSWER - NO WINNER!")