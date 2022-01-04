#Password Generator Project
import random
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

my_password = []
for x in range(0, nr_letters):
    my_password.append(random.choice(letters))
for x in range(0, nr_symbols):
    my_password.append(random.choice(symbols))
for x in range(0, nr_numbers):
    my_password.append(random.choice(numbers))

#print("".join(my_password))
#without join :
my_pass = ""
for x in my_password:
    my_pass += x
print(my_pass)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle((my_password))
my_pass = ""
for x in my_password:
    my_pass += x
print(my_pass)

#we could use while loop and make it much shorter,
#but today's goal was just use for loops and ranges