#Password Generator Project
import random
lc_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
              'y', 'z']
uc_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
              'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrl_letters = int(input("How many lower case letters would you like in your password?\n"))
nru_letters = int(input("How many upper case letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
print("\nEasyLevel Password Generator\n")
password = ""

for char in range(1, nrl_letters + 1):
    password += random.choice(lc_letters)

for char in range(1, nru_letters + 1):
    password += random.choice(uc_letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print("Your easy generated password is:", password, "\n\n")

#Hard Level
print("Hard Level Password Generator\n")

password_list = []

# to add characters to list can use .append or +=
# both are valid

for char in range(1, nrl_letters + 1):
    password_list.append(random.choice(lc_letters))

for char in range(1, nru_letters + 1):
    password_list.append(random.choice(uc_letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print("Here are the randomly chosen password characters:", password_list)
random.shuffle(password_list)
print("Here are the shuffled password characters:", password_list)

password = ""
for char in password_list:
    password += char

print(f"Your hard generated password is: {password}")
