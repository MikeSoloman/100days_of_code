#Tip calculator
print("\n")
print(100 * "*")
print(42 * "*" + " TIP CALCULATOR " + "*" * 42)
print(100 * "*")

#Welcome to the tip calculator
print("\n")
print(100 * "*")
print(35 * "*" + " Welcome to the TIP CALCULATOR " + "*" * 34)
print(100 * "*")


#asks for percentage of the tip customers would like to give
print("What's the total of your bill? \n")
total_bill = float(input(""))
print("What's the percentage of the tip you would like leave? \n")
total_tip = float(input(""))
#and ask about split the bill on how many people
print("How many people are splitting the bill and the tip? \n")
num_of_people = int(input(""))
#and shows how much each person should pay

my_math = (((total_tip / 100) * total_bill) + total_bill) / num_of_people
print(f"The total amount due per person is $ {my_math:.2f}")

#we could use round(n, 2) func instead of {:.2f} but when there is only one number
#after the decimal, with round func it doesn't add 0 ath the end...for example:
# total 150, tip 12, and num of ppl 5, gives us 33.6 instead of 33.60 with round function