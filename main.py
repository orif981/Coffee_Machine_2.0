from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
my_money_machine=MoneyMachine()
my_coffee_maker=CoffeeMaker()
on=True
try:
    while on:
        response=input("What would you like to do?(Coffee/Ingredients/Profit/Off)\n").lower()
        if response=='coffee':
            coffee=input(f"What coffee would you like?({menu.get_items()[:-1]}): \n")
            drink=menu.find_drink(coffee)
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
        elif response=='ingredients':
            print(my_coffee_maker.resources)
        elif response=='profit':
            print(f"${my_money_machine.profit}")
        elif response=='off':
            print("GoodBye!")
            on=False
        else:
            print("Not available")
        if response=='coffee':
            print("\n")
except:
    print()


