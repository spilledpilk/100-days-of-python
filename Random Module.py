import random
#import my_module
# This imports the random module created by the Python team

# random_integer = random.randint(1,10)
# This calls the random module and randint is the function we call it to use with the dot '.'
# Randint calls upon you to assign values for 'a' and 'b' to specify a range of values to
# randomize for. In this case, you want a random number from 1 to 10 (including 1 and 10).
# In PyCharm, you don't need to type in a: or b: as it does that automatically. You may
# simply type in (1,10) and it does the formatting itself.
# print(random_integer)

# So what is a module? It's essentially an in-built function
# that we can refer back to. Similar to a proclib in JCL.

# How do we create our own modules?
# Step 1. go to the side of the course and create a new python file titled my_module
# Inside my module, let's say we create a variable titled:
# my_favorite_number = 3.1415

# Step 2. Go back to the course's task.py.
# When you're working on a project, it could be called something like main.py or app.py
# Basically the primary file where we put in our starting or core code.

# Step 3. Same as the previous module,
# import my_module
#
# Now it's good to use like the random module. In this case, we're printing the function we created in that module.

#print(my_module.my_favorite_number)

# Now when we print, it will produce 1-10 and 3.1415

# Now I comment out my_module and the related code.

# Now let's talk about random floating point numbers.
# Refer back to the documentation and scroll down to

# Real-valued distributions
# The following functions generate specific real-valued distributions.
# Function parameters are named after the corresponding variables
# in the distribution’s equation, as used in common mathematical
# practice; most of these equations can be found in any statistics
# text.
# random.random()
# Return the next random floating-point number in the
# range 0.0 <= X < 1.0
# This is one of the core functions we deal with in Python so remember it:

#random_number_0_to_1 = random.random() * 10
# note that the first random is the module and the second is the
# function called random which pulls in real-valued distributions.
# Use empty parentheses. This doesn't take an input.
# Some functions don't take any input, but still require parentheses
# to carry out the action they're supposed to perform.
#print(random_number_0_to_1) # This will generate from 0.0 to 1.0
# with the * 10, we actually change the range of the values generated
# to 0.0 and 10.

# random_float = random.uniform(1,10)
# print(random_float)
# Seems pretty similar to random.random() * 10
# The only difference is that it's not entirely sure whether you
# will get 10 or not in the random float
# But if you want to be really sure of the range...
# random.random() = semi open range
# random.random always includes 0, but may never include 1.
# random.uniform can get the upper bound or may not.
# As before, you only need to put in the values (1,10) and pycharm
# autocorrects.
# Description:
# random.uniform(a, b)
#
# Return a random floating-point number N such that a <= N <= b for
#     a <= b and b <= N <= a for b < a.
#
# The Number will be greater than or equal to the lower bound and less
# than or equal to the upper bound.
#
# The end-point value b may or may not be included in the range
# depending on floating-point rounding in the
# expression a + (b-a) * random().

# Now for a heads or tails program.
# How would I get this to work?
# I can think of two ways. Odds and evens or 1s and 2s.
# Let's do both:
# print("Heads")
# print("Tails")

# Coinflip = input('I\'m flipping a coin. "Heads" or "Tails." Call it: ').lower()
# random_number = random.randint(1,2)
# # print(random_number)
# if random_number == 1:
#     print("It was Heads")
#     if Coinflip == "heads":
#         print("you win")
#     else:
#         print("you lose")
# else:
#     print("It was Tails")
#     if Coinflip == "tails":
#         print("you win")
#     else:
#         print("you lose")


# Coinflip = input('I\'m flipping a coin. "Heads" or "Tails." Call it: ').lower()
# random_number = int(random.random() * 10) # Note to self. Turning this into an int works
# print(random_number) # - Testing successful
# if random_number % 2 == 0:
#     print("It was Heads")
#     if Coinflip == "heads":
#         print("you win")
#     else:
#         print("you lose")
# else:
#     print("It was Tails")
#     if Coinflip == "tails":
#         print("you win")
#     else:
#         print("you lose")


# Last method is using random.uniform and picking from a range.

#coinflip = input('I\'m flipping a coin. "Heads" or "Tails". Call it: \n').lower()
#random_number = int((random.uniform(1,10)))
#print(random_number) # Testing...
#if coinflip != "heads" or coinflip != "tails":
#    print("pick a real choice")
#else:
#    if random_number <= 5:
#        print("It was heads")
#        if coinflip == "heads":
#            print("you win")
#        else:
#            print("you lose")
#    else:
#        print("it was tails")
#        if coinflip == "heads":
#            print("you lose")
#        else:
#            print("you win")

# Probably my least favorite, but I think it would work really well with this tweak
# random_number = int((random.uniform(1,10)))
# Technically if you just don't type heads or tails, there's a chance you can win at these.
# So here's an extra statement:
# if coinflip != "heads" or coinflip != "tails":
#     print("pick a real choice")

# From Angela
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("heads")
else:
    print("tails")
