# Previously, we would store single values into variables such as assigning states to their
# individual variables like so:
# state1 = "Delaware"
# state2 = "Pennsylvania
# and so on until each state had its own variable.
states_of_america_test = ["Delaware", "Pennsylvania"]
# We can continue this list and add as many values as we want in this data structure.
# We can use lists to store many pieces of related data, but we can also determine the order.
# And that order is determined by their placement within the list.
# So Delaware is the first piece of data, and Pennsylvania is the second.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# So here, if we wanted to take a look at say, the first state that joined first, we could print the variable
# and the placement/index I want to look for. Remember that programmers count from 0, not 1.

print(states_of_america[0])

# Delaware
#
# Process finished with exit code 0
            #0          1       2
fruits = ["Cherry", "Apple", "Pear"]

# Why do we count from 0? Well, if you consider it in offsets, then Cherry here is at the initial
# starting position and Apple is that offset by one position. Pear is two, and so on.
# In many programming languages there are similar data structures to lists and they all start
# from 0.
#If you see square brackets next to a variable, you may be dealing with a list.
#You use square brackets to assign a list of values in a variable, and you also use square brackets to pull from an index within that list.

# print(states_of_america[2]) would be offset by 2 and give us Jersey, the third state.
# You can also pull backwards in the index.
print(states_of_america[-2]) # Alaska

# You may also change a value within a list through the index in the square bracket:
states_of_america[1] = "Pencilvania"

# Print the states now, and you'll get something different:
#print(states_of_america)
# Results:
# ['Delaware', 'Pencilvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']
# Process finished with exit code 0

# You may also add items to the list:
states_of_america.append("angelaland")
# Now when we print this, the new state should appear at the end of the list.
print(states_of_america)
# ...Alaska', 'Hawaii', 'angelaland']

# And remove:
states_of_america.remove("Delaware")
print(states_of_america)
# ['Delaware', 'Pencilvania', 'New Jersey', 'Georgia', 'Connecticut', .... 'Hawaii', 'angelaland']
# ['Pencilvania', 'New Jersey', 'Georgia', 'Connecticut', ....'Hawaii', 'angelaland']

# In addition to appending one item, you may extend the list with another list of items at the end:
states_of_america.extend(["Delaware", "Jack Bauer land"])
# Note that they must be within brackets as you are working with a new list
# Note that they must be contained within their own strings and separated via commas.
# Note that for the extend function to work, they must be within parentheses.
print(states_of_america)
# ... angelaland', 'Delaware', 'Jack Bauer land']

# You needn't memorize functions. That's why we have documentation to refer back to. It's more
# essential to learn how things work. It's better to have a read through and see what you can
# possibly do and understand that information so that next time you run into a situation you
# would want to use those concepts, you could think back on it and google search or parse through
# your notes and documents for the exact methods how to use it. It's better to learn this stuff than memorize.
