# Create a digital coffee machine
from menu_items import MENU
from menu_items import resources


def prompt():
    """ prompts user to select a drink or type 'report' for inventory report """
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == 'exit':
        return
    elif user_request == 'report':
        check_inventory()
        prompt()
    else:
        check_resources(user_request)
        handle_coin(user_request)
        prompt()


def check_inventory():
    for item in resources['amount'].keys():
        if item == 'money':
            print(f"{item.title()}: {resources['units'][item]}{resources['amount'][item]}")
        else:
            print(f"{item.title()}: {resources['amount'][item]}{resources['units'][item]}")


def check_resources(drink):
    """ Checks if enough ingredients are present to make drink and modifies inventory"""
    ingred = MENU[drink]['ingredients'].keys()
    for key in ingred:
        recipe_amount = MENU[drink]['ingredients'][key]
        inventory_amount = resources['amount'][key]

        if recipe_amount > inventory_amount:
            print(f"Not enough {key.title()} in machine to make an {drink}")
            exit()


# Could make this into two functions - one to process coin and one to make drink
def handle_coin(drink):
    """ Takes coins from user, determines if enough coin to make drink.
    If yes, makes drink and adds money to resources. If no, refunds money
    to user. """

    print("Please insert coins.")
    user_coin = int(input("how many quarters?: \n")) * 0.25
    user_coin += int(input("how many dimes?: \n")) * 0.10
    user_coin += int(input("how many nickles?: \n")) * 0.05
    user_coin += int(input("how many pennies?: \n")) * 0.01

    if user_coin < MENU[drink]['cost']:
        print(f"Sorry that's not enough money. Money refunded.")
    elif user_coin > MENU[drink]['cost']:
        change = user_coin - MENU[drink]['cost']
        update_inventory(drink)
        print(f"Here is your ${'%.2f' % change} in change.")
    else:
        update_inventory(drink)

    print(f"Here is your {drink}. Enjoy!")


def update_inventory(drink):
    """ If enough coin and ingredients, modify the inventory """
    resources['amount']['money'] += MENU[drink]['cost']
    ingred = MENU[drink]['ingredients'].keys()
    for key in ingred:
        recipe_amount = MENU[drink]['ingredients'][key]
        resources['amount'][key] -= recipe_amount


prompt()


