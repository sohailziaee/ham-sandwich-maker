# sandwich_maker.py

class SandwichMaker:

    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_name, ingredients):
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"Here is your {sandwich_name}. Enjoy!")