#Function - code you want to use repeatedly

#def my function():
#  Do This
#  Then Do This
#  Finally Do This

#Function with inputs
#def my function(something):
#  Do This With something
#  Then Do This
#  Finally Do This

#Functions with Outputs
#def my function():
#  Do This With something
#  Then Do This
#  Finally Do This

#return tells function that it is the end

def format_name1(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}\n"


#Storing output in a variable
formatted_name = format_name1(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name1(input("What is your first name? "), input("What is your last name? ")))

#Return as an early exit
def format_name2(f_name, l_name):
    # Below is a docstring that will appear as function description
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        #early return
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}\n"

#Storing output in a variable
formatted_name = format_name2(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name2(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
output = len("Javier Soto")
print(f"Length of output = {output}.")

format_name2()