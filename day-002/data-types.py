
# Data Types
# Python is a strongly typed language
# Python keeps track of all variable types

# String
print("Hello"[0])
print("Hello"[4])

print("123" + "345")

# Integer

print(123)
print(123 + 345)

print(123_456_789)

# Float

print(3.14159)

# Boolean: True or False

print(True)
print(False)

# len and data type conversions

num_char = len(input("What is you name?"))
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))

b = (70 + float("100.5"))
print(b)
print(type(b))

c = (str(70) + str(100))
print(c)
print(type(c))


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
# print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)
