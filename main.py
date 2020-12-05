"""
A simple virtual coffee machine
has 3 flavors : espresso, cappuccino and latte
accepts 4 coin types : penny = 1 cent, dime = 10 cents
                        nickle = 5 cents, and quarter = 25 cents
The machine is filled with some resources like milk, coffee, and water
you can modify these resources in the menu.py file

I have followed a To-do list and examples to make it simple for you to comprehend

You can type also 'report' in the console to check available resources
            'off' to switch off the machine for maintenance

*** Author: Chisom Umunnakwe
*** Mentor: Dr. Angela Yu of Appbrewery
"""

from menu import MENU, resources

resources["money"] = 0

# initial price conversion in dollars
one_penny = 0.01
one_dime = 0.1
one_nickle = 0.05
one_quarter = 0.25

is_successful = True


def money_available():
    return resources["money"]


def milk_available():
    return resources["milk"]


def coffee_available():
    return resources["coffee"]


def water_available():
    return resources["water"]


# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
"""
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

"""


def question_prompt():
    """prompt to ask customer their choice of want"""
    prompt_question = input("What would you like? (espresso/latte/cappuccino): ")
    return prompt_question


# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.

""""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
"""


def turn_off():
    print("Machine is now turned off")
    global is_successful
    is_successful = False
    return


# TODO 5:  Process coins

"""
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

"""


def process_coins():
    """Checks to know if there is enough resources"""
    if check_resources(choice):
        print("Please insert coins.")
        quarter_request = int(input("How many quarters?: "))
        dime_request = int(input("How many dimes?: "))
        nickle_request = int(input("How many nickles?: "))
        penny_request = int(input("How many pennies?: "))
        coins_inserted = (quarter_request * one_quarter) + (dime_request * one_dime)
        total_coins_inserted = coins_inserted + (nickle_request * one_nickle) + (penny_request * one_penny)
        return round(total_coins_inserted, 2)
    else:
        print("Sorry there's not enough resource")
        global is_successful
        is_successful = False


# TODO 3: Print report.


""""
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5


"""


def print_report():
    """Prints to the console the available resources"""
    print(f"water: {water_available()}ml")
    print(f"milk: {milk_available()}ml")
    print(f"coffee: {coffee_available()}g")
    print(f"money: ${money_available()}")


# TODO 4: Check resources sufficient?

"""
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.

"""


def water_needed(drink_choice):
    return MENU[drink_choice]["ingredients"]["water"]


def milk_needed(drink_choice):
    return MENU[drink_choice]["ingredients"]["milk"]


def coffee_needed(drink_choice):
    return MENU[drink_choice]["ingredients"]["coffee"]


def check_resources(drink_choice):
    """Checks the resources of the coffee machine"""
    if drink_choice not in MENU:
        print("no available choice")
        global is_successful
        is_successful = False
        return
    water_required = water_needed(drink_choice)
    coffee_required = coffee_needed(drink_choice)
    milk_required = milk_needed(drink_choice)
    if drink_choice == "espresso":
        if water_available() >= water_required and coffee_available() >= coffee_required:
            return True
    elif drink_choice == "latte" or drink_choice == "cappuccino":
        if water_available() >= water_required and coffee_available() >= coffee_required and milk_available() >= milk_required:
            return True

# TODO 6: Check transaction successful?


"""
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.

E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.


"""


def check_transaction_successful(requested_drink):
    """Checks if inserted amount is sufficient"""
    inserted_amount = process_coins()
    drink_amount = MENU[requested_drink]["cost"]
    money_in_bag = money_available()
    if inserted_amount == drink_amount:
        print("There you go")
        print(f"Here is your {requested_drink} ☕ enjoy!")
        money_in_bag += drink_amount
        return money_in_bag
    elif inserted_amount > drink_amount:
        money_in_bag += drink_amount
        change = inserted_amount - drink_amount
        print(f"Here is ${round(change,2)} in change")
        print(f"Here is your {requested_drink} ☕ enjoy!")
        return money_in_bag
    else:
        print("Sorry that's not enough money. Money refunded")
        global is_successful
        is_successful = False
        return


# TODO 7: Make Coffee.

"""
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.

"""


def make_coffee():
    """Offers the coffee to the customer on successful resources"""
    if check_resources(choice):
        resources["money"] = check_transaction_successful(choice)
        milk_required = milk_needed(choice)
        remaining_milk = milk_available() - milk_required
        water_required = water_needed(choice)
        remaining_water = water_available() - water_required
        coffee_required = coffee_needed(choice)
        remaining_coffee = coffee_available() - coffee_required
        resources["water"] = remaining_water
        resources["milk"] = remaining_milk
        resources["coffee"] = remaining_coffee

    else:
        print("Sorry there's not enough resource")
        global is_successful
        is_successful = False


while is_successful:
    choice = question_prompt()
    if choice == "report":
        print_report()
    elif choice == "off":
        turn_off()
    else:
        make_coffee()
