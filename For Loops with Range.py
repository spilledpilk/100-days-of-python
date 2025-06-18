#student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(range([student_scores])) # Needs to be used in conjunction with another function. In this case, it'll be used with for.
#
# maximum = 0
# for score in student_scores:
#     if score > maximum:
#         maximum = score
# print(maximum)
# # Angela's solution. Fairly similar.

# Here's my revised minimum too:
# minimum = 10000000
# for score in student_scores:
#     if score < minimum:
#         minimum = score
# print(minimum)

#
# # Up till now, we've only being using for loops in association with lists'
# # for item in list_of_items:
# #     #Do something to each item

# for number in range(1, 11):     # Running this between 1-10 will only give us the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. To specify 10, we need to use values 1,11
#     print(number)

# By default, range will go through each value listed 1 by 1. If you wanted to skip through 2 or more, you would need to increase the value with an additional comma to specify how large you want the step size to be.
# for number in range(1, 11,3):
#     print(number)

# Gauss Challenge.
# We want to essentially take the last value and the first value and add them all up, I think

total_sum = 0
first_num = 0
second_num = 0
for number in range(1,101):
#    print(number)       # All this will do is print numbers 1 - 100.
    if number < 51:
        first_num = number
        second_num = 101 - number
        total_sum += first_num + second_num
print(total_sum)

# first number should be incrementing(
# second should be decrementing
# total should add up both

#print(sum(range(1,101)))        # Harr harr. This gets me the result, but I learned nothing.

# Angela's solution:
# total = 0
# for number in range(1,101):
#     total += number
# print(total)

# Ya dumbass. You overcomplicated it.
# It's literally just 1 + 2 + 3.. the freaking way the teacher intended for it to be done.
