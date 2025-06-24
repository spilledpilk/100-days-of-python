# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
# for student in student_scores:
#     print(student_scores[student])
#     if student_scores[student] >= 91 or student_scores[student] >= 100:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] >= 81 or student_scores[student] >= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] >= 71 or student_scores[student] >= 80:
#         student_grades[student] = "Acceptable"
#     elif student_scores[student] <= 70:
#         student_grades[student] = "Fail"
#
# for score in student_grades:
#     print(score)
#     print(student_grades[score])
# print(student_grades)

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#print Lille
# How would we pull that info?
#print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# How would pull the value "D" from this Nested list?
print(nested_list[2][1])
# We've actually already done this in the past with the dirty dozen.
# The first number pulls from the index of where the second nested list starts. In this case, 2.
# Then the second number specifies the index where D is located. In this case, 1, since we count from 0.


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited": ["Stuttgart", "Hamburg", "Berlin"],
        "total_visits": 5
    },
}
# So here we have lists and strings within dictionaries within another dictionary.
# Our data is more complex. We have more key values associated and a much better way of organizing our travel log.
# How can we print Stuttgart from this travel log?
# Got to figure out how to access the Germany dictionary then the cities_visited list and finally that item in the list.

#print(travel_log["Germany"])    # This prints out Germany's values.
print(travel_log["Germany"]["cities_visited"][0])   # This is how you get Stuttgart.
# Dictionary[Dictionary2][List][Index] <= This is the syntax.

