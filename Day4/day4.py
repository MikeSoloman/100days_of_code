# Day 4 coding challenge was submitted one day late because a
#severe snow storms and extreme power outages in my area
#which left close to 120,000 people without electricity for
#almost 26-27 hrs... but positive thing is that I have managed to
#make a 8 ft snowman :)

#Todays's challenge will be on randint, random, and making 2 games:
#head or tail & rock, paper, scissors games, keep in mind that I can easily
#make this game more code comples, but the whole reason of my
#100 days of code challenge is to start with baby steps and achieve
# advanced level, therefore, it will be a very simple game. Happy Coding :)


#head or tail
# from random import randint
# head_or_tail = randint(0, 1)
# user_guess = 0
# while True:
#     print("Please just type head for head or tail for tail")
#     user_guess = input("Type head / tail:\n").lower()
#     if head_or_tail == 0:
#         head_or_tail = "head"
#     else:
#         head_or_tail = "tail"
#     if user_guess == head_or_tail:
#         print(f"Congrats, you have guessed it right\n"
#             f"Your pick was {user_guess} and coin was {head_or_tail}")
#         yes_no = input("Do you want to play again? y/n ? ").lower()
#         if yes_no == "y":
#             user_guess = None
#             head_or_tail = randint(0, 1)
#         else:
#             print("Thanks for playing")
#             break
#     else:
#         print(f"Sorry you lost....\n"
#             f"Your pick was {user_guess} and coin was {head_or_tail}")
#         head_or_tail = randint(0, 1)

#rock, paper, scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# from random import choice
# user_pick = None
# choices_of_game = [rock, paper, scissors]
# while True:
#
#     print("Please type either rock, paper, or scissors")
#     user_pick = input("\n").lower().strip()
#     comp_pick = random.randint(0, 2)
#     if user_pick == "rock":
#         user_pick = 0
#     elif user_pick == "paper":
#         user_pick = 1
#     else:
#         user_pick = 2
#
#     if user_pick == comp_pick:
#         print(f"WOWWWWWW, it's even, you have picked:\n"
#               f"{choices_of_game[user_pick]}\n and computer have picked:\n"
#               f"{choices_of_game[comp_pick]} ")
#     elif user_pick == 0 and comp_pick == 2:
#         print(f"WOWWWWWW, YOU WON, you have picked:\n"
#               f"{choices_of_game[user_pick]}\n and computer have picked:\n"
#               f"{choices_of_game[comp_pick]} ")
#     elif user_pick == 1 and comp_pick == 0:
#         print(f"WOWWWWWW, YOU WON, you have picked:\n"
#               f"{choices_of_game[user_pick]}\n and computer have picked:\n"
#               f"{choices_of_game[comp_pick]} ")
#     elif user_pick == 2 and comp_pick == 1:
#         print(f"WOWWWWWW, YOU WON, you have picked:\n"
#               f"{choices_of_game[user_pick]}\n and computer have picked:\n"
#               f"{choices_of_game[comp_pick]} ")
#     else:
#         print(f"SORRY YOU HAVE LOST, you have picked:\n"
#               f"{choices_of_game[user_pick]}\n and computer have picked:\n"
#               f"{choices_of_game[comp_pick]} ")
#     print("would you like to play again? ")
#     yes_no = input("y/n ? ").lower()
#     if yes_no == "y":
#         user_pick = None
#         comp_pick = random.randint(0, 2)
#     else:
#         print("Thanks for playing... bye bye")
#         break
