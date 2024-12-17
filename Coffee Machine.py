MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

coin_value = {"quarter": 0.25,
              "dimes": 0.10,
              "nickles": 0.10,
              "penny": 0.01,
              }
machine_cash = 0
day_sold = 0
cost = 0
water_needed = 0
milk_needed = 0
coffee_needed = 0

def coffee_choice(coffee):
    global cost, water_needed, milk_needed, coffee_needed, machine_cash
    cost = MENU[coffee]["cost"]
    water_needed = MENU[coffee]["ingredients"]["water"]
    milk_needed = MENU[coffee]["ingredients"]["milk"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    machine_cash += cost
    print(f'A {coffee} cost ${cost}.')

def check_resources(resource):
    items_out = 0
    for item in MENU[resource]["ingredients"]:
        if MENU[resource]["ingredients"][item] > resources[item]:
            print("Sorry" if items_out == 0 else "")
            print(f'We are short of {item}')
            items_out += 1
    if items_out > 0:
        return False
    else:
        return True

def cash():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    penny = int(input("How many penny?: "))
    return (coin_value["quarter"] * quarter) + (coin_value["dimes"] * dimes) + (coin_value["nickles"] * nickles)  + (coin_value["penny"] * penny)

def coffee_machine():
    global day_sold
    turn_off = False
    while turn_off is False:
        resources["water"] = resources["water"] - water_needed
        resources["milk"] = resources["milk"] - milk_needed
        resources["coffee"] = resources["coffee"] - coffee_needed
        action = str(input(f'What do you like? (espresso/latte/cappuccino):'))
        if action in ["espresso", "latte", "cappuccino"]:
            if check_resources(action) is True:
                coffee_choice(action)
                money = cash()
                if money < cost:
                    print("You didn't insert enough coins")
                else:
                    print("Enjoy your coffe!!!")
                    print(f'Your change is {money - cost}')
                    day_sold += 1
            else:
                print("Call someone for help")
                turn_off = True

        elif action == "report":
            print(f'Today we sold {day_sold} coffee')
            print(f'The amount of chash in the machine is ${machine_cash}')
            for item in resources:
                print(f'The level {item} is {resources[item]}g ')
        elif action == "turn off":
            turn_off = True

coffee_machine()
