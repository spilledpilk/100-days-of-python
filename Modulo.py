Number = int(input("Please type in a number and I will tell you if it odd or even: "))

if Number % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")
# Things to note...
# Don't forget that the colon should be after the entire if statement.
# You must convert the input in the Number variable to an integer to be used for an equation
# You needn't type out something like Number % 2 != 0 for the else statement. It's implied by the if
# It'd be good to check a few things as you're programming. Here are a few now:
# print(Number) - Just see if your number is coming out the way you want it.
# print(type(Number)) - This will tell you if properly turned it into an integer.
# print(Number % 2) - This here will tell you if your modulo is working right.
# Remember that = 0 is different from == 0. One's an assignment, the other is checking equality.
# Finally you may remove all those and prepare your conditional statements as in your solution.
