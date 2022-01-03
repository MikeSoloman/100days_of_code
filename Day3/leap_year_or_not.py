#this was an interesting video challenge and I have decided
#to add it to my exercise

#The goal of the challenge is to take an input and tell the person
#if an year they have entered is a leap year or not

#the criterea is pretty simple, if an year evenly divisable by 4
#it is a leap year, unless it's also evenly dividable by 100, then it's not, but if
#it's divisable evenly by 100 and 400, then it's leap year....

pick_an_year = int(input("Enter any year "))

if pick_an_year % 4 == 0:
    if pick_an_year % 100 == 0 and pick_an_year % 400 == 0:
        print("Leap")
    elif pick_an_year % 100 == 0:
        print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")
