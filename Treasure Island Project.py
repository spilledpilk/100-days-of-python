print(r'''
                                             ////////
       Maybe this could be you!!             |:---[.]
                 =====>                      |(     _J
                                             | ^ ( _|
                                            / \_____)
                                           /  _____  \
                                          |  /     \  \
         _________                        |  |     |   |
       ./       ./                        \  /\   /\__ |
     ./       ./ |                        |  |        \/---
   ./        ./  |                        \   \            )\
  /________ / o  |                         |   >_____/_____)\
  |        |     |                         \__________/
  |        |     |__  ________             /         \
  |        |    /  ./ ------- .\           |          |
  |        |   / ./            \.\         \          \\
  |        |  /  (              ) )         \          |\
  |        | /    \.          ./ /           \         | \
  !--------------\ \._______./ /              \         | |
  !               `============'               |        |  |
   \                       I                  |       |   |
    >                      I                 |        /   |
   /                        \               |________/____|
  <                          >              (_________)____)  -MH/cfbd-
___\________________________/________   _____________________
''')
print("You knew you really shouldn't have had that much coffee and oatmeal.")
print("BUDDY, YOU'RE PACKING. GET THE HELL TO THE BATHROOM ASAP.")
print("Alright. You're at your buddy's place and you dunno where to go.")
direction = input("You see a fork ahead and two paths before you. Left or Right? \n")
# First ask the user left 'or' right.
# OK
fail_safe = "huh? Did you mistype? Start over."

if direction == "Right" or direction == "right":
    print("Sorry. You came up to a bathroom, but the door's locked! You browned. Try again.")
# If they choose right or any other condition, game over
# Not to self. direction == needs to be specified at every turn.
# OK
elif direction == "Left" or direction == "left":
    print("It's a good thing you came here. I think the bathroom might have been the other way")
# If they choose left, wait 'or' charge
    take_action = input("You've got a whole line ahead. What are they all waiting for? Do you Wait or Charge?\n")
    if take_action == "wait" or take_action == "Wait":
        print("Good job. Did you forget you were in a rush? You're shitsing... Try again.")
# If they waited, game over
# OK
    elif take_action == "charge" or take_action =="Charge":
        print("You've got no time to lose. You make your way to the kitchen!")
        finale = input("This is it. The final frontier. Do you use the Sink? The Freezer? The Window?\n")
# Pick a final option. Freezer 'and' Window are game overs. Sink is a win.
        if finale == "Sink" or finale == "sink":
            print("You did it! You won! You finally relieved yourself! Make sure to take the dishes out next time!")
        elif finale == "Freezer" or finale == "freezer":
            print("What? Why did you pick this? It's too high. You peed yourself. Try again.")
        elif finale == "Window" or finale == "window":
            print('''Could this be your window of opportunity?
Sorry, no.
It was just too far for you to get to in time.
Unfortunately you made a fool of yourself in front of a total babe too. Ouch...
Try again.''')
        else:
            print(fail_safe)
    else:
        print(fail_safe)
else:
     print(fail_safe)




# Few things to consider:
# Be creative with your game overs.
# Make sure capitalization is considered. right 'and' Right should both be considered.
# 3 Single quotes (''') allow you to create multiple lines of a string.
# To reiterate, do NOT forget the == when specifying and/or/not statements.
# Seriously. I had to use Thonny to go through my stuff step by step.


# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a crossroad, where do you want to go? '
#                 'Type "Left" or "Right".\n').lower()
# # Hitting enter here actually does the sensible thing of breaking up the line and formatting it
# # properly under the one before with indentation.
#
# # You can actually use single quotes instead of double quotes if you want to include
# # them in as part of the text. For example
# # print('Please say "Hello"'')
# # The issue with doing it here is because of the word you're.
# # The way to deal with that is using '\'. This backslash symbol is interpreted as an escape function
# # in programming. It means we're trying to escape this symbol so don't interpret it as our code.
# # You could have also typed 'you are at', but this is going to suck long term.
# # One way to cut out my "== or" problems is to just add a .lower()/.upper at the end of the choice.
# # This makes it so even if I typed "Right", "rIGHT", or whatever, it would all end up as "right".
# # Remember = is assigning a value, and == is equalizing.
# if choice1 == "left":
# # You could have typed choice1 == left or choice1 == Left. These are perfectly valid as well as lower()
# # Continue in the game
#     choice2 = input('You\'ve come to a lake. '
#                     'There is an island in the middle of the lake.'
#                     'Type "wait" to wait for a boat.'
#                     ' Type "swim" to swim across.\n').lower()
# # To avoid the double quotes and single quotes getting interpreted, we can use backslashes.
# # But since this line is too long, we ought to use triple single quotes and also break up our string.
# # Again, we can also use single quotes and hit enter.
# # Choice2 MUST be indented in Choice1.
#     if choice2 == "wait":
#     # game will continue
#         choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game over.")
#         elif choice3 == "yellow":
#             print("You found the treasure. You win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game over.")
#         else:
#             print("You chose a door that doesn't exist. Game over.")
#     else:
#         print("You got attacked by an angry trout. Game over.")
#
# if choice1 == "right":
#     # Results in game over. This makes a lot more sense.
#     print("You fell into a hole. Game Over.")
#
