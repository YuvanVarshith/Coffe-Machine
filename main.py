MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

counter_balance = 0


def money(coffe_type):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if coffe_type == "espresso" and amount < 1.50:
        return "Sorry that's not enough money. money refunded"
    elif coffe_type == 'latte' and amount < 2.50:
        return "Sorry that's not enough money. money refunded"
    elif coffe_type == 'cappuccino' and amount < 3.00:
        return "Sorry that's not enough money. money refunded"
    else:
        return amount


def remaining_resources(coffee):
    if coffee == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif coffee == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif coffee == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24


def make_coffee():
    global counter_balance
    is_resources_over = False
    while not is_resources_over:
        user_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
        if user_choice == "report":
            print(
                f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney ${counter_balance} ")
        elif user_choice == "espresso":
            if resources["water"] < 50:
                print("Sorry there is not enough water")
            else:
                available_amount = money("espresso")
                if available_amount != "Sorry that's not enough money. money refunded":
                    change = available_amount - 1.5
                    counter_balance += available_amount - change
                    perfect_change = format(change, '.2f')
                    print(f"Here is ${perfect_change} in change")
                    print(f"Here is Your latte ☕. Enjoy!")
                    remaining_resources("espresso")
                else:
                    print(available_amount)
        elif user_choice == 'latte':
            if resources["water"] < 200:
                print("Sorry there is not enough water")
            else:
                available_amount = money("latte")
                if available_amount != "Sorry that's not enough money. money refunded":
                    change = available_amount - 2.5
                    counter_balance += available_amount - change
                    perfect_change = format(change, '.2f')
                    print(f"Here is ${perfect_change} in change")
                    print(f"Here is Your latte ☕. Enjoy!")
                    remaining_resources("latte")
                else:
                    print(available_amount)
        elif user_choice == 'cappuccino':
            if resources["water"] < 250:
                print("Sorry there is not enough water")
            else:
                available_amount = money("cappuccino")
                if available_amount != "Sorry that's not enough money. money refunded":
                    change = available_amount - 3.0
                    counter_balance += available_amount - change
                    perfect_change = format(change, '.2f')
                    print(f"Here is ${perfect_change} in change")
                    print(f"Here is Your latte ☕. Enjoy!")
                    remaining_resources("cappuccino")
                else:
                    print(available_amount)
        elif user_choice == 'off':
            is_resources_over = True


make_coffee()
