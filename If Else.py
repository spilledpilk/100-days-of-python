print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")  # Do NOT write else right below print. Should go below if
else:
    print("Sorry you have to grow taller before you can ride.")
# if height > 120:
# This statement doesn't actually cover 120, meaning when you run the code, you'll still get a message saying you're not tall enough to ride.
#
# > greater than symbol.
#
# You can include 120 by using the >= symbols, greater than and equals.
# Running the code again will work now.
#
# < less than
# <= less than or equal to
# == equal to
# != Not equal to
#
# It's important to remember that...
# ONE equal sign '=' means you are assigning a value to that specific variable.
# TWO equal signs '==' means that you are checking equality between the values on the left and right and they're completely different.
# Usually you will get a SyntaxError saying you've got an invalid syntax if you miss a sign.
