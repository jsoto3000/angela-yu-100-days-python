#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip percentage would you like to give? 10%, 12%, 15%, 17%, or 25%? "))
people = int(input("How many people to split the bill?"))

#long form
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount1 = round(bill_per_person, 2)

#short form
final_amount2 = round(bill * (1 + tip / 100) / people, 2)

#formatted to two decimal places
final_amount3 = "{:.2f}".format(bill_per_person)

print(f"Long form: Each person should pay: ${final_amount1}")
print(f"Short form: Each person should pay: ${final_amount2}")
print(f"Formatted to two decimal places: Each person should pay: ${final_amount3}")
