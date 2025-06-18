fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:    # What this does is it takes this list of values, "fruits", and assigns a variable "fruit" to each item in the list.
    print(fruit)
    print(fruit + " pie")
# So essentially what happens in a for loop is it assigns the item in fruits to variable fruit
# processes the lines of code within the block
# So in this case, prints fruit = apple then prints fruit = apple + pie
# before moving onto the next item where it'll repeat the process by assigning peach to the variable fruit and printing that out and so on.
# When you see an indentation after a colon, all of those instructions are within a block of code for that statement
#    print(fruits)   # Printed like this within the block of code, we will see the following:
# Apple
# Apple pie
# ['Apple', 'Peach', 'Pear']
# Peach
# Peach pie
# ['Apple', 'Peach', 'Pear']
# Pear
# Pear pie
# ['Apple', 'Peach', 'Pear']
print(fruits)   # Take this one outside of that indentation, and it will only be printed once
# Apple
# Apple pie
# Peach
# Peach pie
# Pear
# Pear pie
# ['Apple', 'Peach', 'Pear']
