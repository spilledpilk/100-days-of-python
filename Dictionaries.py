programming_dictionary = { # A good way to maintain readability is leaving the curly brace on top and indenting the key/value entries.
    "Bug": "An error in a program that prevents the program from running as expected.", # <= You also want to hit enter after every entry to keep them in their own lines for readability.
    "Function": "A piece of code that you can easily call over and over again.", # Be sure to add commas at the end of your dictionaries so that you can easily add more entries to the list. This will avoid headaches later on if you forget and end up adding two entries in one.

} # <= And cap off with a final curly brace below the initial dictionary definition.

#print(programming_dictionary["Bug"])
# Important to actually spell the key correctly when fetching information.
# Common to make typos.
# You will get a KeyError highlighting the line where you typed in a Key that cannot be found because it doesn't exist.

#print(programming_dictionary["Bug"])
#This will NOT contain Loop. Only Bug and Function.

programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)
# Now it will have all of them.

#programming_dictionary = {}
#print(programming_dictionary)

#That can be useful to restart things like scores and stats.

#Can also use this to edit an item in a dictionary.

#programming_dictionary["Bug"]
# Redefine its value. Currently, "An error in a program that prevents the program from running as expected."

# Can redefine like adding a new entry with the Loop example. Basically the equal sign will redefine the value or add a new key and value if that key doesn't exist.
programming_dictionary["Bug"] = "A moth in your computer."

#If you print this now, the definition for bug has been changed.
#print(programming_dictionary["Bug"])

#Loop through a dictionary.
for thing in programming_dictionary:
    print(thing)
# What will be printed when I click run?
# I believe it'll be like so:
#{"Bug": "A moth in your computer.","Function": "A piece of code that you can easily call over and over again.","Loop": "The action of doing something over and over again."}
# Ah, wait. Never mind. I had a brain fart. It should print each Key value per item.

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
