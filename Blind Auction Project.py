from art import logo
print(logo)
# TODO-1: Ask the user for input
# Test OK.

# TODO-2: Save data into dictionary {name: price}
# Test OK.

# TODO-3: Whether if new bids need to be added
# Test OK.

# TODO-4: Compare bids in dictionary
#print("Hello")
#print("\n" * 100) # Going to need this to clear the screen.
# Need to add the starting logo.


bidder = {}
winner = ""
highest_bid = 0

auction_end = False
while not auction_end:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidder[name] = price
    if price > highest_bid:
        highest_bid = price
        winner = name


    additional_bidders = input("Are there any other bidders? Type 'yes' or 'no'.: ").lower()
    print("\n" * 20)
    if additional_bidders == "no":
        auction_end = True

print(f"The winner is " + winner + f" with a bid of " + str(highest_bid))


# Angela's code:

# When it comes to a new program, it's a good idea to draw it in a flow chart and break it down in a couple of tasks.
# Ask the user for input. Name, bid, any other bidders.
# We need a way of capturing these inputs. TODO-1.
# We need to save that data into a dictionary {name: price}. TODO-2.
# Whether any new bids need to be added. Loop back to 2. TODO-3.
#should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")


# Compare bids in dictionary. TODO-4.

# import art
#
# print(art.logo)
#
# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     # max(bidding_dictionary, key=bids.get)   # This is an alternative, but the below is better for learning.
#     winner = ""
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder] # <= This is how we get a hold of the value when looping dictionaries.
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")
#
# bids = {}   # <= Keep this outside of the while loop so it doesn't get wiped.
# continue_bidding = True
# while continue_bidding:
#     name = input("what is your name?: ")
#     price = int(input("What is your bid? $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)
