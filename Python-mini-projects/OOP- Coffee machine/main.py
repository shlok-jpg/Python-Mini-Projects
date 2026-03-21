from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem
menu_item = MenuItem
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
menu= Menu()
loop = True
while loop:
    menu.get_items()
    choice = input("What would you like?")
    drink = menu.find_drink(choice)
    if choice == "off":
        loop = False
    elif choice == "report":
        CoffeeMaker.report()
    elif choice == "profit":
        MoneyMachine.report()
    elif CoffeeMaker.is_resource_sufficient(drink):
            MoneyMachine.make_payment(drink.cost)
            CoffeeMaker.make_coffee(drink)
