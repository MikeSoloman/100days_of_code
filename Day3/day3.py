from random import choice
from random import randint
#a simple treasure island game, with simple if else statements

#could add dictionary and through get func or through index pull

#answers, but again, this is lesson 3 and goal is to keep it beginner level

#Happy Coding
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 
                   ''')

print("Welcome to the Treasure Island, your mission is to ......."
      "Find the treasure...... it's pretty dangerous here......"
      "be careful comrade")

user_input = input("Let's start walking, left or right? ").lower().strip()

if user_input != choice(["left", "right"]):
    print("Ohhh nooo... you fall into a hole, game over")
else:
    print("Good choice")
    user_input = input("Let's keep playing, swim or wait? ").lower().strip()
    if user_input == choice(["swim", "wait"]):
        print("Ohhh nooo... you have been attacked by a mysterious monster, game over")
    else:
        print("Good choice")
        user_input = input("Let's keep playing, which door? red, blue, yellow? ").lower().strip()
        if user_input == choice(["red", "blue", "yellow"]):
            print("You made it so far man....lucky comrade!!!!")
            user_input = int(input("last thing, I am thinking about"
                               "a number between 1 and 5..."
                               "you guess it right, you win ").lower().strip())
            my_guess = randint(1, 5)
            if user_input == my_guess:
                print("UNBELIEVABLE !!!!!")
                print("LUCK YOUUUU, YOU HAVE WON")
                print(f"ur guess was {user_input} and I guessed {choice()}")
            elif user_input not in [1, 2, 3, 4, 5]:
                print("Eaten by a giant baby sea star"
                      "because you broke the rules")
            else:
                print("Shame of the motherland, you LOOOOSE")
        elif user_input not in ["red", "blue", "yellow"]:
            print("Eaten by a giant baby sea hawk"
                  "because you broke the rules")
        else:
            print("Shame of the motherland, you LOOOOSE")
