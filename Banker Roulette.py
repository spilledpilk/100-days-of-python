import random
from random import choice

# I figure I'll be using this
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# So first thing to note is friends is already a data structure with 5 items in it.
# We want to access this list and pick an index at random.

# This one just works:
#roulette = random.choice(friends)
#print(roulette)
#Slightly better version:
#print(random.choice(friends))

# I think that's it. There are probably other ways to do this by assigning numbers, but
# This is the most succinct that I've found after perusing the random module page of the
# official documentation.

# After looking at the hints now, I believe this was the intended solution in hint 3.



# Perhaps this method will too, but I don't like it. I'm missing a better way to do this.
# Basically doesn't even take from the friends variable at all.
# winner = "blank"
# spin = random.randint(1,5)
# if spin == 1:
#     winner = "Alice"
#     print(winner)
# elif spin == 2:
#     winner = "Bob"
#     print(winner)
# elif spin == 3:
#     winner = "Charlie"
#     print(winner)
# elif spin == 4:
#     winner = "David"
#     print(winner)
# else:
#     winner = "Emanuel"
#     print(winner)
# # Not a fan of this result. It works, but I haven't applied what I've learned in the previous
# # Section.


roulette_spin = random.randint(0,4)
# can use random int to generate a random number. Yes.
print(friends[roulette_spin])
# Oh, my God. I did it. I just figured what if I replaced the number of the index with
# the roulette spin variable. That's great. This was the intended solution, I'm pretty sure.
