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
#----------------------------------------------ORDER FUNCTION--------------------------------------------------
def order():
    for a in MENU[Choice]["ingredients"]:
        if resources[a] < MENU[Choice]["ingredients"][a]:
            print(f"Sorry, you cannot get a {Choice}!")
            cycle = "off"
            break
        else:
            resources[a] -= MENU[Choice]["ingredients"][a]
            print("Enter coins to proceed.")
            q = float(input("Quarters:"))*0.25
            d = float(input("Dimes:"))*0.10
            n = float(input("Nickles:"))*0.05
            p = float(input("Pennies:"))*0.01
            coins = q+d+n+p
            if coins >= MENU[Choice]["cost"]:
                change = coins - MENU[Choice]["cost"]
                print("Your Change is: ", change)
                print(f"Enjoy your {Choice}!")
            elif coins < MENU[Choice]["cost"]:
                print("Insufficient funds!")
                break
            break
#------------------------ ask for input ---------------------------------------------------------------------
machine = "on"
while machine == "on":
    Choice = input("What would you like? (espresso/latte/cappuccino):")
    if Choice == "off":
        machine = "off"
        break
    elif Choice == "report":
        for key , value in resources.items():
            print(f"{key}: {value}")
    else:
        order()



#-------------------------------------------------------------------------------------------------------------

