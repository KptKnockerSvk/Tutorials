from source_data import MENU
from source_data import resources

# === Basic serrings ===
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]



# === Funcions ===
def report(data):
    print(f"Water: {data['water']}")
    print(f"Milk: {data['milk']}")
    print(f"Coffee: {data['coffee']}")

def coins():
    print("Insert coins of type 1, 2, 5, 10, 20, 50 ")
    kc1  = int(input("Sum of 1s "))
    kc2  = int(input("Sum of 2s "))  * 2
    kc5  = int(input("Sum of 5s "))  * 5
    kc10 = int(input("Sum of 10s ")) * 10
    kc20 = int(input("Sum of 20s ")) * 20
    kc50 = int(input("Sum of 50s ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"All in all inserted {suma} money")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Drink is boiling")
        if refund > 0:
            print(f"Here is refund money: {refund}")
    else:
        print(f"Not enough money. Insert another {price - user_sum_coins} money")

def fill_in_ingredience():
    return resources

def consumption_ingredience(name_of_drink, ingredience):
    if name_of_drink == "e":
        name_of_drink = "espresso"
    elif name_of_drink == "l":
        name_of_drink = "latte"
    elif name_of_drink == "c":
        name_of_drink = "cappuccino"

    ingredience["water"] = ingredience["water"] - MENU[name_of_drink]["ingredients"]["water"]
    ingredience["milk"] = ingredience["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
    ingredience["coffee"] = ingredience["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]

def calculate_ingredients(drink_name):
    if drink_name == "e":
        consumption_ingredience(drink_name, rest_of_ingredience)
    elif drink_name == "l":
        consumption_ingredience(drink_name, rest_of_ingredience)
    elif drink_name == "c":
        consumption_ingredience(drink_name, rest_of_ingredience)

def ingredience_checker(in_water, in_milk, in_coffe):
    if in_water < 0:
        print("Not enough water")
        return False
    elif in_milk < 0:
        print("Not enough milk")
        return False
    elif in_coffe < 0:
        print("Not enough coffee")
        return False
    else:
        print("All good")
        return True


# === Dispencer code ===
rest_of_ingredience = fill_in_ingredience()

lets_continue = True

while(lets_continue):
    user_choice = input("What would you like to order ? (espresso/latte/cappuccino): ")

    calculate_ingredients(user_choice)

    if user_choice == "report":
        report(resources)
    elif user_choice != "report":
        lets_continue = ingredience_checker(rest_of_ingredience["water"], rest_of_ingredience["milk"], rest_of_ingredience["coffee"])

    if lets_continue == False:
        break


    if user_choice == "e":
        sum = coins()
        print(f"Price of esspresso is: {espresso_price} money")
        calculate_change(sum, espresso_price)
    elif user_choice == "l":
        sum = coins()
        print(f"Price of latte is: {latte_price} money")
        calculate_change(sum, latte_price)
    elif user_choice == "c":
        sum = coins()
        print(f"Price of cappuccino is: {cappuccino_price} money")
        calculate_change(sum, cappuccino_price)

