from coffe_maker import CoffeeMaker
from menu import *
from money_machine import MoneyMachine


'''Let's create all the objects we'll use'''
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? {options}')

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(choice)

        if  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)







