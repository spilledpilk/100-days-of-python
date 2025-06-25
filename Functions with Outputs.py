# def format_name(f_name, l_name):        # Will take these parameters as inputs whenever this gets called.
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name("anGeLa","YU"))
# # len already does this by capturing the length of a variable as an input then producing that number as an output.
# # And we can further store that variable within a variable name like so:
# output = len("Angela")
#
# # What is the difference between a return statement and print?

# Take for instance a function that doesn't print its output at all.
def function_1(text):
    return text + text


def function_2(text):
    return text.title()

# Neither of these functions have a print statement.
# output = function_1("Hello")
# print(output)
# Now how would we use function_1 as the input for function_2?
output = function_2(function_1("hello"))
print(output)
