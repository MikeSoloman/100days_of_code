############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from random import randint, random, choice
from logo import art

# BLACK JACK, FIRST WAY TO DO IT

print("WELCOME TO ........................ ")
print(art)
user_input = input("Do you want to play comrade? or You are scaaaareddd....?\n"
                   "Type y to play, or n if you are looking for mommy and scared  ").lower()

while user_input == 'y':

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_random_cards = [choice(cards), choice(cards)]

    computer_random_cards = [choice(cards)]

    comp_score = sum(computer_random_cards)

    user_score = sum(user_random_cards)

    print(f"Your cards : {user_random_cards}, current score is : {user_score})")
    print(f"Computers first card: {computer_random_cards}")

    extra_card = input("Type 'y' to get another card, type 'n' to pass:  ").lower()

    while extra_card == "y" and user_score < 21:

        user_random_cards.append(choice(cards))
        user_score = sum(user_random_cards)

        print(f"Your cards : {user_random_cards}, current score is : {user_score})")
        print(f"Computers first card: {computer_random_cards}")

        if user_score > 21:
            break
        extra_card = input("Type 'y' to get another card, type 'n' to pass:  ").lower()

    if extra_card == 'n' or user_score > 21:

        while comp_score <= 17:
            computer_random_cards.append(choice(cards))
            comp_score = sum(computer_random_cards)

        print(f"Your cards : {user_random_cards}, your score is : {user_score})")
        print(f"Computers cards : {computer_random_cards}, computer score is : {comp_score})")

    if user_score <= 21 and comp_score <= 21:
        if user_score > comp_score:
            print("You Woooon")
        elif user_score == comp_score:
            print("its a draw")
        else:
            print("Computer Wonnn, better luck next time comrade")
    elif user_score > 21:
        print("You went over, you lose")
    elif user_score <= 21 and comp_score > 21:
        print("You Woooon")
    else:
        print("You went over, you lose")

    user_input = input("\nDo you want to play comrade? or You are scaaaareddd....?\n"
                       "Type y to play, or n if you are looking for mommy and scared  ").lower()


