#today's coding challenge is about combining for and while loops and
#using reeborg robot challenges

#challenge #1 was to creat new functions that will make the robot
#to go from point a to point b with as little code as possible:

#link for challenge:
# "https://reeborg.ca/reeborg.html?lang=en&mode
# =python&menu=worlds%2Fmenus%2Freeborg_intro_en
# .json&name=Hurdle%201&url=worlds%2Ftutorial_en
# %2Fhurdle1.json"

#my solution:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def walk():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for x in range(0, 6):
#     walk()

#challenge #2 hurdle2, random finish line, robot has to stop at
#any place computer picks a finish line, link for challenge:
# "https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=
# worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url
# =worlds%2Ftutorial_en%2Fhurdle2.json"

#My solution:
#def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def walk():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while at_goal() != True:
#     walk()
# or
# while not at_goal:
#     walk()

#Challenge 3:
#Reeborg has entered a hurdle race. Make him run the course, following
# the path shown. The position and number of hurdles changes each time
# this world is reloaded. What you need to know The functions move()
# and turn_left().The conditions front_is_clear() or wall_in_front(),
# at_goal(), and their negation.How to use a while loop and an if statement.

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#Really challenging, took a good time to solve:
#Lost in a maze Reeborg was exploring a dark maze and the battery in
# its flashlight ran out. Write a program using an if/elif/else
# statement so Reeborg can find the exit. The secret is to have
# Reeborg follow along the right edge of the maze, turning right
# if it can, going straight ahead if it can’t turn right, or turning
# left as a last resort.
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds
# %2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2
# Fmaze1.json

#My Solution

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#while front_is_clear():
#       move()
#turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()