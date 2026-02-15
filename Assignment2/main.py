# main.py

import data
import sandwich_maker
import cashier

resources = data.resources
recipes = data.recipes

sandwich_machine = sandwich_maker.SandwichMaker(resources)
cash_register = cashier.Cashier()

is_on = True

while is_on:
    choice = input("What would you like? (ham_sandwich): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(resources)

    elif choice in recipes:
        recipe = recipes[choice]
        ingredients = recipe["ingredients"]
        cost = recipe["cost"]

        if sandwich_machine.check_resources(ingredients):
            payment = cash_register.process_coins()

            if cash_register.transaction_result(payment, cost):
                sandwich_machine.make_sandwich(choice, ingredients)