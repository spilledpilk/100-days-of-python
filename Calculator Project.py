def add(n1, n2):
    return n1 + n2

# TODO-1: Write out the other 3 functions - subtract, multiply, divide
# Done.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+, "-", "*", "/".
# Done.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO-3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# Done. First the dictionary, then the key in square brackets, and finally the inputs n1,n2 in parentheses.
# print(operations["*"](4,8))
# Test OK.

# TODO-5: Print logo
# Test OK.
from art import logo
#print(logo)


# TODO-4: Need to loop the above function and retain the original number if the person wants it.
# Test OK.

test = True
reuse_first = ""
number_1 = ""
while test:
    if reuse_first == "y":
        number_1 = result
    if reuse_first != "y":
        print("\n" * 20)
        print(logo)
        number_1 = float(input("What is your first number?\n"))
    math_operator = input("Choose your mathematical operator: '+', '-', '*', '/' \n")
    number_2 = float(input("What is your second number?\n"))
    #result = (operations[math_operator](number_1,number_2))
    result = operations[math_operator](number_1, number_2)
    print(number_1, math_operator, number_2, "=", result)
    reuse_first = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: \n").lower()

# Angela's solution:
# def calculator():
#     print(logo)
#     should_accumulate = True
#
#     num1 = float(input("What is the first number?: "))
#
#     while should_accumulate:
#
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ").lower()
#
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
#
# calculator()
