# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

#Write your code below this line

years = 80 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

message = (f"You have {days} days, {weeks} weeks, and {months} months left.")
print(message)
