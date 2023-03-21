#Calculator2

from os_clear import clear
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        # print vs return
        # return allows you to pass over returned output to another function as input

        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(first_answer, num3)
        print(f"{first_answer} {operation_symbol} {num2} = {second_answer}")

        if input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = second_answer
        else:
            should_continue = False
            clear()
            #recursion: function calls itself
            #be careful with while loops and recursion (can end up with an infinite loop)
            calculator()

calculator()
