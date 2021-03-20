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


# TODO: 1.Print report of all coffeeMachine resources


def print_remaining_resources():
    print(f"Water: {report_water}ml")
    print(f"Coffee: {report_coffee}ml")
    print(f"Milk: {report_milk}ml")
    print(f"Money: ${round(report_money,2)}")

# TODO: 2.Check the coins - Process coins


def calculate_coins ():
    print("Please insert coins.")
    nr_quarters = float(input("how many quarters?: "))
    nr_dimes = float(input("how many dimes?: "))
    nr_nickels = float(input("how many nickels?: "))
    nr_pennies = float(input("how many pennies?: "))
    total_amount = round( (nr_quarters * 0.25) + (nr_dimes * 0.1)+ (nr_nickels * 0.05) + (nr_pennies * 0.01), 2)
    # print(total_amount)
    return total_amount

# TODO: 3.Check the inventory Check resources sufficient?


def check_inventory(product):
    water_needed = MENU[product]["ingredients"]["water"]
    coffee_needed = MENU[product]["ingredients"]["coffee"]
    # other option is to add the key milk in the dictionnary for espresso with a value of 0
    # MENU["espresso"]["ingredients"]["milk"] = 0
    if product == "espresso":
        milk_needed = 0
    else:
        milk_needed = MENU[product]["ingredients"]["milk"]

    if water_needed > report_water:
        print(f"Sorry there is not enough water.")
        return False
    elif coffee_needed > report_coffee:
        print(f"Sorry there is not enough coffee.")
        return False
    elif milk_needed > report_milk:
        print(f"Sorry there is not enough milk.")
        return False
    else:
        return True

# TODO: 8.Check the payment


def check_payment(coins_amount, product):
    money_needed = MENU[product]["cost"]
    # print(money_needed)
    change = round(coins_amount - money_needed, 2)
    if change < 0:
        # te weinig betaald, maw geen product
        return change
    else:
        # teveel of genoeg betaald, maw product & refund
        print(f" Here is $ {change} dollars in change.")
        return change

# TODO Process the order


def process_order(revenue, product):
    # increase revenue
    global report_money
    report_money += revenue

    # reduce inventory
    global report_water
    global report_coffee
    global report_milk
    report_water -= MENU[product]["ingredients"]["water"]
    report_coffee -= MENU[product]["ingredients"]["coffee"]
    if product != "espresso":
        report_milk -= MENU[product]["ingredients"]["milk"]

    # print the order
    print(f"Here is your {product}. Enjoy!")


# initialization

report_money = 0
report_water = resources["water"]
report_milk = resources['milk']
report_coffee = resources['coffee']
coffeeMachine_running = True

# TODO: 4.Prompt user by asking “ What would you like? (espresso/latte/cappuccino):


while coffeeMachine_running:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_choice == "report":
        print_remaining_resources()
    elif (coffee_choice == "espresso") or (coffee_choice == "latte") or (coffee_choice == "cappuccino"):
        # check the inventory
        if check_inventory(coffee_choice):
            coins_amount = calculate_coins()
            # TODO: 6.Check transaction successful
            if check_payment(coins_amount, coffee_choice) >= 0:
                # genoeg betaald & genoeg voorraad
                revenue = MENU[coffee_choice]["cost"]
                # print_remaining_resources()
                # TODO: 7.Make Coffee.
                process_order(revenue, coffee_choice)
                # print_remaining_resources()
            else:
                print("Sorry that's not enough money. Money refunded. ")
        else:
            check_inventory(coffee_choice)
    # TODO: 5.turn off the Coffee Machine by entering “ off ” to the prompt.
    elif coffee_choice == "off":
        coffeeMachine_running = False





