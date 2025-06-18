import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Basically you're going to take all of these lists, pull a number of random items from each list in accordance to the user's input specifications
# And randomly combine them all in the end.
# Easy version is to generate them all in sequence.
# I imagine the logic would be something like password = nr_letters + nr_symbols + nr_numbers
# Maybe I'll shoot for that one first then go for the more complicated one.

# Easy Level. Let's go.

# password_gen = 0
# letter_gen = 0
# symbol_gen = 0
# number_gen = 0
# I think I'm going to have to use integers to pull a random index out of these lists.
# Basically right now I want to create a block of code that will pull that many letters out of my letters based on the user's input
# Figure this out, and you can apply it to the other two
# So say I choose 5 letters in my password. nr_letters = 5
# Now I will take letters and pick 5 random items from it.
# Going to need to use the random module.

# Randomly found random.shuffle(x). I think this might be used in the hard version.
# random.randrange might be worth looking at too.
# for letter in letters:
#     if nr_letters != 0:
#
# I think I want to assign a value with nr_letters and run that loop that many times with the for statement.

# I think I essentially want to take the input as the number of loops to specify in the for statement
# Then use a random.randint to grab a random value from the index.
# Just not sure how to do the first part yet

letter_gen = 0
number_gen = 0
symbol_gen = 0
ordered_password_gen = ""           # This was literally all I needed. OH MY GOD, I HATE THIS. I'VE BEEN STUCK FOR AGES.
for number in range(0,nr_letters):
    letter_gen = (random.choice(letters)) # This right here will produce a random letter x amount of times the user asked for. I just need something to combine all that information incrementally.
    ordered_password_gen += letter_gen
# I need to take these values and combine them into a list.
# We're getting somewhere. With this block of code, I can generate random items from this list according to the user's input.
for number in range(0,nr_symbols):
    symbol_gen = (random.choice(symbols))
    ordered_password_gen += symbol_gen
#    print(passwordgen2)
for number in range(0,nr_numbers):
    number_gen = (random.choice(numbers))
    ordered_password_gen += number_gen
#   print(passwordgen3)
# I repeated the process twice, and now I have all the values to form a password.
print(f"Your sequential password is {ordered_password_gen}")
# This is the easy version. This will be acceptable. I combined all the gens into one sequence.
# For the hard version, I think what I want to do is take the previous generations and scramble them.
# Now for the hard version. Add this:
shuffle = list(ordered_password_gen) # To shuffle, I must first list all the characters in the previous string individually again. This effectively creates a new list like so:
# shuffle = [number of items from letters, number of items from numbers, number of items from symbols] so if I picked 3, 4, 5, I would get something like this in here [a, b, c, +, -, (, ), 1, 2, 3, 4, 5]
random.shuffle(shuffle) # This command was the one I found earlier. It will shuffle all the characters so they are no longer in sequence
shuffled_password = "".join(shuffle) # Now I will join my list into one single string again effectively turning the jumbled up shuffle list from earlier into a new single value string like say, "45a+-bc(12)3" or whatever
print(f"Your password is {shuffled_password}") # Now I can just print the result and hand that to someone.
# Damn, I must be a genius!



# Angela's Easy version
#password = "" #GOD, THIS WAS LITERALLY THE FIRST THING SHE DID. THIS WOULD HAVE SAVED SO MUCH TIME.
# nr_letters = 4 # Let's pretend the user selected this
#for char in range(1,nr_letters + 1): # Because programming starts from 0 and what not, we're creating a range from 1 to x characters. But the user isn't actually getting the number he specified unless we add an additional +1 at the end of our range
    # 1 - 4
    #random_char = random.choice(letters)
    #print(random_char) # Gives us each letter
    # How do we combine them? We can use the string concatenation we learned VERY early on. Damn, I actually checked that too..
    #password = password + random_char
    #password += random_char    # This was the same logic I followed. I just wasn't getting it because I missed the password: "" for the longest time
    #print(password)    # so this runs the loop several times and you see the letters getting appended in each run. The way to fix this is to run the print the one time
#print(password)    # running this here would have it run the one time.
#Just need to do the same for the number and symbols too:
#for char in range(1, nr_symbols + 1):      # Note. My original method of 0, nr_symbols and so on is actually valid instead of 1, nr_symbols + 1. Good to know.
    #password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# Angela's Hard version
# Instead of adding these letters into a string, we actually want to add it to a list.
#password_list = []

#for char in range(0, nr_letters):
    #password_list += random.choice(letters)
    #Here's an alternative:
    #password_list.append(random.choice(letters)) # I KNEW IT. APPEND.
#for char in range(0, nr_symbols):
    #password_list += random.choice(symbols)
#for char in range(0, nr_numbers):
    #password_list += random.choice(numbers)
# print(password_list)

# How to change the order of items in a list in python? Google that. You'll come across random.shuffle(x)
#random.shuffle(password_list)
#print(password_list)   # now we'll get the shuffled version. If only we could turn this back into a string...
# Could use a for loop.
#password = ""
# for char in password_list
#   password += char
#print(f"Your password is: {password}")
# And that's gg.
