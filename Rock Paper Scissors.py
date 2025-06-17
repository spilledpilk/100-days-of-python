import random
# I will probably need this.

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

# Here we have the ASCII art and three move variables, rock, paper, and scissors.
#print(rock)     # => Test ASCII art

moves = [rock, paper, scissors]
results = ["You win","You lose","It's a draw"]
# Might need a variable like this.


# Tasks and thoughts...

# Decide who won/lost.
# Choose how computer picks a random shape.
# Get the game to work like the final version.
# Could have a list for just the rock/paper/scissors results lists


players_move = int(input('It\'s Rock, Paper, Scissors time. Type 0 for "Rock", 1 for "Paper", or 2 for "Scissors"\n').lower())
# Okay, I think this is the logical start. I added lower there too.
# Turn it into an integer so it can be used for the index.
print("You chose:\n")
if players_move >= 0 and players_move <= 2:
    print(moves[players_move])



comp_choice = random.randint(0,2)
print("Computer chose:\n")
print(moves[comp_choice])
# Randomizes the computer


# Now to compare.
if  players_move >= 3 or players_move < 0:      # Failsafe.
    print("Invalid number. You lose.")
elif comp_choice == players_move:
    print(results[2])
elif comp_choice == 2 and players_move == 0: # scissors beaten by rock
    print(results[0])
elif comp_choice == 0 and players_move == 1: # rock beaten by paper
    print(results[0])
elif comp_choice == 1 and players_move == 2: # paper beaten by scissors
    print(results[0])
else:
    print(results[1])

# 34 - 71 for original code.
# Drawing the logic on something like draw.io can make visualizing your challenge a lot easier.
# Another good practice is testing your code along the way. Makes it easier to pick up bugs as you're working on things.

# 77 - 99 for solution
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
# # 0, 1, or 2
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])
#
# computer_choice = random.randint(0,2)
# print(f"Computer chose: ")
# print(game_images[computer_choice])
#
# if  user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")
