student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# What if we wanted to work out the total exam score?
# Add up all the numbers up together.
# Python has the "sum" for any iterable data type including lists.

total_exam_score = sum(student_scores)
print(total_exam_score)

# This is a helpful function developed by the Python team, but we can actually replicate this
# Ourselves using for loops.

sum_of_results = 0
for score in student_scores:
    sum_of_results += score
# First we created the variable 'sum'.
# Then we created the loop that will run through every item in the student_scores list and
# have 'sum' be equal to each item on the list + the next item per time it loops.
# Essentially this will add up all the integers on the list and run just like the actual
# sum function.
print(sum_of_results)

# This is a way to use the building blocks of Python to build out functionality for various use cases such as summarizing the numbers of a list and adding them up.

# Now to replicate the "max" Python function:

print(max(student_scores))

max_score = student_scores[0] # This will give it the value 150.
for score in student_scores:    # This will run through the list and assign each item to score while running the block of code
    if max_score <= score:      # If score is higher than max_score, it will replace it
        max_score = score
print(max_score)        # Will produce 199

maximum = 0
for score in student_scores:
    if score > maximum:
        maximum = score
print(maximum)
# Angela's solution. Fairly similar.

# For funsies, here's min_score too:

min_score = student_scores[0] # This will give it the value 150.
for score in student_scores:    # This will run through the list and assign each item to score while running the block of code
    if min_score >= score:      # If score is lower than min_score, it will replace it
        min_score = score
print(min_score)        # Will produce 24

# Here's my revised minimum too:
minimum = 10000000
for score in student_scores:
    if score < minimum:
        minimum = score
print(minimum)

# I think in a hypothetical where you have too many numbers and don't know what could be the highest, you ought to go with the original method of assigning one of the values from the list to it.
