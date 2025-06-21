# def greet(name):
#     print(f"Hello {name}")
#     print(f"How do you do?")
#     print(f"How's the weather?")
# greet("tommy")


def life_in_weeks(age):
    # Idea is to calculate the number of weeks the person has left assuming they live to 90 years old.
    age *= 52  # This is the number of weeks per year.
    # There are 4680 weeks in 90 years. If you were 56, you'd have spent 2912 weeks already.
    # Need to subtract 2912 from 4680 for a result of 1768 weeks left.
    result = 4680 - age
    print(f"You have {result} weeks left.")


life_in_weeks(56)
# We can't use input as there is no console. We must simply type in an age that we'd like to test.
# In this case, 12.
