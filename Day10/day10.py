from art import logo
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():

    print(logo)

    num1 = float(input("Whats the first number? "))

    for key in operations.keys():
        print(key)

    user_answer = 'y'

    while user_answer == 'y':
        operation_symbol = input("Pick an operation from these options: ").strip()
        num2 = float(input("Whats the next number? "))
        simple_math = operations[operation_symbol]
        answer = simple_math(num1, num2)
        print(answer)
        user_answer = input(f"Type 'y' to continue calculating with your answer\n"
                            f"{answer} or type 'n' to start all over: ").lower().strip()
        if user_answer == 'y':
            num1 = answer
            continue
        else:
            clear()
            calculator()
            break


calculator()
