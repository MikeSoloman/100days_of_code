#idea is that Your life in week, comparing it to a 90 yr old life span
#show how many days, weeks, and months left if you will make it to 90 from ur current age

your_age = float(input("What's your age comrade? \n"))

#we could use while loop in case if user inputs negative numbers, or
#if no numbers were entered, or if user have used any letters, while loop would
#keep asking for a valid input, but this exercise for beginner level, hence,
#i am just going to assume that user does what he/she supposed to do :)

months_left = round((90 * 12) - (your_age * 12), 2)
weeks_left = round((90 * 52) - (your_age * 52), 2)
days_left = round((90 * 365) - (your_age * 365), 2)

#we could easily do the math inside of the curly brackets without making
#variables first, but this way it's more clean for beginners to understand

print(f"You got {months_left} months, {weeks_left} weeks, "
      f"and {days_left} days left ... have fun till you can :) ")