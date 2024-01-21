#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 500
        self.coffee_beans = 200
        self.cups = 10
        self.money = 0

    def display_resources(self):
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee Beans: {self.coffee_beans}g\nCups: {self.cups}\n")

    def take_order(self, choice):
        menu = {
            '1': {'name': 'Espresso', 'water': 250, 'milk': 0, 'coffee_beans': 16, 'cost': 4},
            '2': {'name': 'Latte', 'water': 350, 'milk': 75, 'coffee_beans': 20, 'cost': 7},
            '3': {'name': 'Cappuccino', 'water': 200, 'milk': 100, 'coffee_beans': 12, 'cost': 6}
        }

        if choice in menu:
            drink = menu[choice]
            if self.can_make(drink):
                print(f"Making {drink['name']}...")
                self.water -= drink['water']
                self.milk -= drink['milk']
                self.coffee_beans -= drink['coffee_beans']
                self.cups -= 1
                self.money += drink['cost']
                print(f"{drink['name']} is ready! Enjoy your coffee!\n")
            else:
                print(f"Sorry, not enough resources to make {drink['name']}. Please refill.\n")
        elif choice == 'back':
            return
        else:
            print("Invalid choice. Please try again.\n")

    def can_make(self, drink):
        return self.water >= drink['water'] and self.milk >= drink['milk'] and                self.coffee_beans >= drink['coffee_beans'] and self.cups >= 1

    def refill_resources(self):
        self.water = 1000
        self.milk = 500
        self.coffee_beans = 200
        self.cups = 10
        print("Refilled resources in the coffee machine!\n")

    def display_money(self):
        print(f"Money Earned: ${self.money}\n")


def main():
    coffee_machine = CoffeeMachine()

    while True:
        print("=== Coffee Machine ===")
        print("1. Display Resources")
        print("2. Take Order")
        print("3. Refill Resources")
        print("4. Display Money Earned")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            coffee_machine.display_resources()
        elif choice == '2':
            order_choice = input("Choose your coffee (1 - Espresso, 2 - Latte, 3 - Cappuccino, 'back' to go back): ")
            coffee_machine.take_order(order_choice)
        elif choice == '3':
            coffee_machine.refill_resources()
        elif choice == '4':
            coffee_machine.display_money()
        elif choice == '5':
            print("Exiting the Coffee Machine. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()


# In[ ]:




