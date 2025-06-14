name = "Angela"
length = len(name)
print(length)
# Name your variables whatever you like as long as you're consistent and don't screw up using them,
# but keep best practices in mind. They'll help you and everyone else. Mainly you.
# One of these is making your variables clear.
#
# Because yeah, if you come back to your code in a couple months,
# variables like N and L aren't really gonna mean anything to you.
# Which will lead to needless troubleshooting when you could have typed up some comments and stuff,
# dude
#
# Make sure it makes sense to you.
# If you want, you can actually use multiple words in your variable.
# You would just separate the words with an underscore. DO NOT use spaces.
# It will give you a syntax error.
# You can use numbers in your variables, but not in the beginning.
# This will also generate a syntax error.
# There are certain privilege words we use such as the names of our functions like Print and Input.
# Don't use them. Syntax highlights them because it thinks you're actually
# trying to use the function. And even though your program might not actually have any problems,
# it's really confusion and really bad practice so don't do it.
#
# Watch out for typos when you name your variables.
# So for example, let's say you throw down a function that refers back to that variable later on.
# name = "Angela"
# length = len(nama)
#
# You'll get what is called a:
# NameError: name 'nama' is not defined
#
# And all that's saying is your variable name is non-existent.
# It'll be highlighted so you can just check your names and fix that.
#
# You could also just go with nama instead of name in the first place. No issues whatsoever.
#
# You'll have a green squiggly telling you nama's a typo, but it doesn't matter for your program.
#
# You could have a character in your game called Nama, for example.
# It's all good.Basically so long as you're consistent with it, your variable's one name,
# your function refers to it and not some typo or something else, then you're fine.
#
# When you get a name error in your code, it's because you probably mistyped your variable
# somewhere in your code.
#
# Got an exercise down below. Basically this won't work because Midnight is capitalized
# Leading to a NameError. The variable I'm referring to doesn't exist.
# time_until_midnight = "5"
# print("there are "+time_until_Midnight+" hours until midnight")
