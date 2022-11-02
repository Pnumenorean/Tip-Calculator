# Welcome message
print("Welcome to the Tip Calculator!")

# Assigning the total bill as a float to the bill variable
bill = float(input("What was the total bill?: $"))
# Assigning the tip amount as an interger to the tip variable
tip = int(input("How much tip would you like to give? 15, 18, or 20?: "))
# Assigning the total people as an interger to the people variable
people = int(input("How many people are splitting the bill?: "))

# Calculating the total bill
total_bill = tip / 100 * bill + bill
# Calculating the total each person has to pay
bill_per_person = total_bill / people
# Rounding what each person has to pay to 2 decimal places
final_amount = round(bill_per_person, 2)

# String outputting the amount each person has to pay
print(f"Each person should pay: ${final_amount}")
