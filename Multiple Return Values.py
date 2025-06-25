def format_name(f_name, l_name):
    """"Take a first and last name and format it to return
     the title case version of the name."""
    if f_name == "" or l_name == "":
        #return # Just a blank return. Nothing after. This will cancel the rest of the function in the case of this if statement where you don't type a thing in the inputs and get hit with None on return.
         return "You did not provide valid inputs"    # This is better since it actually tells the user what they did wrong. This is an empty Return.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
    #print("This got printed")   # This line actually doesn't run. Return tells the code that that's the end of the function.


print(format_name(input("What is your first name?"), input("What is your last name?"))) # Now what happens is it will ask for an input and take these two inputs and call that function and return the formatted version to be printed.
# Now it's possible we didn't give it a first or last name.

# How can we get the function to bypass the rest of the code if they type in an empty first name or last name? Answer: Early Return statement.

# Is it a leap year? Here's the proper code to check:
def is_leap_year(year):
    """This function allows you to input a year and check if it is a leap year or not."""
    if year % 4 != 0:
        return False
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    return None

print(is_leap_year(1700))


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)
