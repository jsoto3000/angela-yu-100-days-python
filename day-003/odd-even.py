'''
Intro to Modulo %

Modulo returns returns the remainder or signed remainder of 
a division, after one number is divided by another 
(called the modulus of the operation). 
'''

a = 7 % 2
b = 7 % 3

print("Modulo of 7/2 = ", a)
print("Modulo of 7/3 = ", b)

# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
    print("This is an odd number.")
