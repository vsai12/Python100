from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
cm_obj = CoffeeMaker()
money_obj = MoneyMachine()

on = True
while on:
    choice = input(f"What would you like? ({menu_obj.get_items()}): ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        cm_obj.report()
        money_obj.report()
    else:
        item = menu_obj.find_drink(choice)
        if item is not None:
            if cm_obj.is_resource_sufficient(item):
                if money_obj.make_payment(item.cost):
                    cm_obj.make_coffee(item)
