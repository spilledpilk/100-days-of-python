# Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")  # <= Needs to be an f-string
#     print(f"How's the weather in {location}?") # <= Use both parameters as declared initially in the function.
#
#
# greet_with("Jack Bauer", "Nowhere") # <= When you call this function, it will prompt you to add name and location
#
# greet_with("Nowhere", "Jack Bauer") # <= Positional Argument. Parameters are unspecified so they refer to the positions within the function to assign functionality.
#
# greet_with(location="Nowhere", name="Jack Bauer") # <= In this case, we are assigning the arguments to the proper parameters.

def calculate_love_score(name1, name2):
    name_check = name1.lower() + name2.lower()
    total_1 = 0
    total_2 = 0
    print(f"{name_check}")
    for letters in name_check:
        if 't' in letters:
            total_1 += 1
        if 'r' in letters:
            total_1 += 1
        if 'u' in letters:
            total_1 += 1
        if 'e' in letters:
            total_1 += 1
            total_2 += 1
        if 'l' in letters:
            total_2 += 1
        if 'o' in letters:
            total_2 += 1
        if 'v' in letters:
            total_1 += 1
    print(f"Love Score is: {total_1}{total_2}")

calculate_love_score("Kanye West", "Kim Kardashian")
# This will definitely work, but I've got an alternate version in store with count()

def calculate_love_score(name1, name2):
    names = name1.lower() + name2.lower()
    true = names.count("t") + names.count("r") + names.count("u") + names.count("e")
    love = names.count("l") + names.count("o") + names.count("v") + names.count("e")


    print(f"Your love Score = {true}{love}")

calculate_love_score("Kanye West", "Kim Kardashian")


# Angela's solution:
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")



#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")
