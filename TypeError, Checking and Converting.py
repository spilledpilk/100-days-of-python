print(len("12345")) # pause 1, I just replaced the integer with a string. Functionally works the same
# in this case anyway...
print(type("hello"))
# This is a string
print(type(123))
# This is an integer
print(type(123.4))
# This is a float
print(type(True))
# This is a boolean. Note the capitalized T.


"123" # We have this string here that we want to turn into an integer.
int("123") # Previously we tried to sum up 123 and 345,
# but since they were strings, they concatenated into 123345
# but with this function, we turned it into an integer.
print("123" + "345") # 123345
# print(int("123") + "345") This will fail since one is an int and the other a str
print(int("123") + int("345")) # Now it'll actually sum them up as integers.
# There are limitations. You can't really convert something like "abc" into a number.
# print(int("abc") + int("345"))
#print("Number of letters in your name: " + str(len(input("Enter your name"))))
name_of_the_user = input("Enter your name ")
length_of_name = len(name_of_the_user)
# Error message is basically saying you can only concatenate strings with strings.
# When you calculate the len, it gives you a number. So it is likely giving you an integer.
# You can type check like so:
print(type("Enter your name "))
print(type(length_of_name))
# Can see the first one is a string and the second an integer. So now you can see what
# was wrong with the initial line of code. All we need to do is wrap the variable in a string
# type conversion. Should work as intended.
print("Number of letters in your name " + str(length_of_name))
