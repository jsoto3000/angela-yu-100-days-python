import random
# Don't change the code below
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
print("random.randint method")
names_as_csv = input("Give me everybody's names, separated by a comma. ")
names = names_as_csv.split(",")
# Don't change the code above

#Write your code below this line
print("Here is the complete list of names: ", names)

#Get the total number of items in list.
num_items = len(names)

print(f"There are {str(num_items)} names in our list")
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(f"Today, {person_who_will_pay} is going to pay for the meal!\n\n")

#code using random.choice() instead
print("random.choice method")
names_as_csv = input("Give me everybody's names, separated by a comma. ")
names = names_as_csv.split(",")
print("Here is the complete list of names: ", names)
person_who_will_pay = random.choice(names)
print(f"Today, {person_who_will_pay} is going to pay for the meal!")

