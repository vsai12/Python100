MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": [300, "ml"],
    "Milk": [200, "ml"],
    "Coffee": [100, "g"],
}


def check_resources(item):
    ing = item["ingredients"]
    for i in ing:
        if resources[i][0] - ing[i] < 0:
            print(f"Sorry there is not enough {i.lower()}.")
            return False
    return True


def process_coins():
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickels?: "))
    p = int(input("how many pennies?: "))
    return 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p


def make_coffee(item):
    ing = item["ingredients"]
    for i in ing:
        resources[i][0] -= ing[i]
    print("Here is your latte. Enjoy!")


on = True
money = 0
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        for r in resources:
            amt = resources[r][0]
            measurement = resources[r][1]
            print(f"{r}: {amt}{measurement}")
        print(f"Money: ${money}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        coffee = MENU[choice]
        enough = check_resources(coffee)
        if enough:
            print("Please insert coins.")
            total = process_coins()
            cost = coffee["cost"]
            if total >= cost:
                money += cost
                change = total - cost
                format_change = "{0:.2f}".format(change)
                if change > 0:
                    print(f"Here is ${format_change} dollars in change.")
                make_coffee(coffee)
            else:
                print("Sorry that's not enough money. Money refunded.")




