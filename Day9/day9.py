import clear

from art import logo

print(logo)

auction_bidders = {}

while True:
    bidders_name = input("Whats ur name comrade? ")
    bidders_price = float(input(f"{bidders_name} what's ur offer? "))

    auction_bidders[bidders_name] = bidders_price

    question_ = input('Are there any other bidders? y/n ').lower()

    if question_ == 'y':
        continue
    else:
        highest_bid = 0
        winner = ""
        for k,v in auction_bidders.items():
            if v > highest_bid:
                winner = k
                highest_bid = v
        print(f"The winner is {winner} and the bid is {highest_bid}")
        break

