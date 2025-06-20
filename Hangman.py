import random
import hangman_words
#from hangman_words import word_list    You could import one list or variable from a module instead.
import hangman_art
#from hangman_art import stages, logo   Can add a comma to import multiple from a module
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# I imported hangman_words for this. I redefined chosen_word so that it would include the word_list from that module. random.choice(hangman_words.word_list)
# Test OK.

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# Test OK. I imported the hangman_art module and referenced the logo item.
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
used_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    # Test OK. I changed the below to an f string and added lives as a variable. As it is already an integer, it will decrement throughout the game.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    # Alright, I've added the line below to print out the same time you lose a life.
    # Test OK.


    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed the letter " + guess + ", that's not in the word. You lose a life!")
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            # Edited it to include the chosen_word variable.
            # Test OK.

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    # I misunderstood thinking that I would need to run this and keep the score the same when the person typed the same wrong letter twice. Nah. I ran the solution and checked. This is all that needs to be done.
    # Test OK.

    if guess in used_letters:
        print("You've already entered this letter. Try another!")
    used_letters.append(guess)
    # I could have just reused correct_letters actually. Oh, well. Works the same. Might even be clearer in a sense.

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    # I imported the hangman_art module. I also changed the below line to reference the stages list in it. hangman_art.stages
    print(hangman_art.stages[lives])
