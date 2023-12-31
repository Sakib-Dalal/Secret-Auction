from art import logo
print(logo)

auction = {}
bid_finnish = False


def find_highest_bidder(my_dict):
    highest_bid = 0
    winner = ""
    for bidder in auction:
        price_from_bidder = auction[bidder]
        if price_from_bidder > highest_bid:
            highest_bid = price_from_bidder
            winner = bidder
    print(f"The winner is: {winner} with a bid of: {highest_bid} Rs.")


while not bid_finnish:
    name = input("What is your name: ")
    price = int(input("What is your bid: "))

    auction[name] = price

    should_continue = input("Are there any other bidders? Type 'Yes' to continue or 'No' to end: ").lower()
    if should_continue == 'yes':
        bid_finnish = False
    else:
        bid_finnish = True

find_highest_bidder(auction)
