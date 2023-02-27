'''
Logic in plain English:
ON every year that is divisible b 4
    EXCEPT every year that is evenly divisible by 100
        unless the year is also evenly divisible by 400
'''

# Don't change the code below
print("Let's verify if the selected year is a leap year.")
year = int(input("What is the  year you want to check? "))
# Don't change the code above

#Refer to the flow chart here: https://bit.ly/36BjS2D

leap_year = True

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
            print("Leap year = ", leap_year, ".")
        else:
            leap_year = False
            print("Leap year = ", leap_year, ".")
    else:
        leap_year = True
        print("Leap year = ", leap_year, ".")
else:
    leap_year = False
    print("Leap year = ", leap_year, ".")
