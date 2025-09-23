from art import coffee_art
from resources import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 3: Print report.
def print_report():
    # print(resources)
    for k in resources.keys():
        if k == "money":
            item = '${:,.2f}'.format(resources[k])
        elif k == "coffee":
            item = str(f"{resources[k]}g")
        else:
            item = str(f"{resources[k]}ml")
        print(f"{k.title()}: {item}")

#  TODO 1: Prompt user “ What would you like? (espresso/latte/cappuccino): ”
def coffee_machine():
    resources["money"] = 0
    ordering = True

    while ordering:
        order = input("What would you like: Espresso, Latte or Cappuccino? ").lower()

        # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
        if order == "off":
            ordering = False
            print("Shutting down ...")
        elif order == "report":
            print_report()
        else:

            ingredients = MENU[order]["ingredients"]
            cost = MENU[order]["cost"]

            # TODO 4: Check resources sufficient?
            for key in ingredients:
                if resources[key] <= ingredients[key]:
                    print(f"Sorry, there is not enough {key}.")
                    serve_coffee = False
                    break
                else:
                    # TODO 5: Process coins.
                    print(f"{order.title()} costs {'${:,.2f}'.format(MENU[order]["cost"])}\nPlease insert your coins: ")
                    print("•••••••••••••••••••••••••••••••••••")
                    quarters = float(input("How many quarters?: "))
                    dimes = float(input("How many dimes?: "))
                    nickels = float(input("How many nickles?: "))
                    amount_paid = quarters * .25 + dimes * .10 + nickels * .05
                    print(f"You paid {'${:,.2f}'.format(amount_paid)}")

                    # TODO 6: Check transaction successful?
                    if amount_paid == cost:
                        serve_coffee = True
                    elif amount_paid > cost:
                        serve_coffee = True
                        amount_difference = cost - amount_paid
                        refund = '${:,.2f}'.format(abs(amount_difference))
                        print(f"{order.title()} is {'${:,.2f}'.format(cost)} ⟶ ⟶ here is {refund} back.")
                    elif amount_paid < cost:
                        print(f"You didn't pay enough, your money is returned.")
                        serve_coffee = False

                    # TODO 7: Make Coffee.
                    if serve_coffee:
                        for key in ingredients:
                            resources[key] -= ingredients[key]
                        resources["money"] += cost
                        print("•••••••••••••••••••••••••••••••••••")
                        print(f"Here's your {order.title()}, Enjoy! {coffee_art} ")
                        break

coffee_machine()