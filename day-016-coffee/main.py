from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Drinks", ["Latte", "Espresso", "Cappuccino"])
table.add_column("Cost", ["$2.50", "$1.50", "$3.00"])

table.align = "l"


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    print(table)
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        is_on = False
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
            is_on = False


