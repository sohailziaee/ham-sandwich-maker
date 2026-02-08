# Sandwich Maker Machine

# Resources available in the machine
resources = {
    "bread": 12,   # slices
    "ham": 18,     # slices
    "cheese": 24   # ounces
}

# Recipes and costs
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}


class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (
            dollars * 1.0 +
            half_dollars * 0.5 +
            quarters * 0.25 +
            nickels * 0.05
        )
        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, ingredients):
        for item in ingredients:
            self.machine_resources[item] -= ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


def print_report():
    print(f"Bread: {resources['bread']} slice(s)")
    print(f"Ham: {resources['ham']} slice(s)")
    print(f"Cheese: {resources['cheese']} pound(s)")


# Main program loop
machine = SandwichMachine(resources)

is_on = True
while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print_report()

    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]

        if machine.check_resources(ingredients):
            payment = machine.process_coins()
            if machine.transaction_result(payment, sandwich["cost"]):
                machine.make_sandwich(choice, ingredients)

    else:
        print("Invalid selection. Please try again.")
