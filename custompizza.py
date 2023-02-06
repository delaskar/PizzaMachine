from menu import INGREDIENTS
from prettytable import PrettyTable
import os


class Custompizza:

    def __init__(self):
        self.category_numbers = []
        self.number_toppings_selected = []  # Store the options of toppings
        self.topping_selected = []  # Store the toppings selected by user

        self.is_On = True
        self.back_off = ''
        self.maximum_toppings = 4
        self.addtion_counter = 0
        self.fixed_price = 10

    def showToppings(self):
        """This method show the Toppings Category"""

        # Create a table category
        oTcatgory = PrettyTable()
        oTcatgory.field_names = ["Number", "Toppings Category"]

        # Store data for a table category
        for key1, value1 in INGREDIENTS.items():
            self.category_numbers.append(key1)
            for key2, value2 in value1.items():
                oTcatgory.add_row([key1, key2])

        print(oTcatgory)

    def availableToppings(self):
        """This method prints a table of the toppings I have available."""

        clear_cmd = 'os.system("clear")'

        # Create a available toppings table
        oTtoppings = PrettyTable()
        oTtoppings.field_names = ["Name Category", "Number", "Available Toppings"]

        # Check if the user input is a number from the Toppings category
        while True:
            user_topping = input("Enter the number of the category you want to see: ")
            if user_topping.isdigit():
                exec(clear_cmd)
                break
            else:
                print("Selection must be a number from category. Try again.")

        # converting the user input to an integer
        user_topping = int(user_topping)

        self.topping_names = []  # Store the name of toppings

        # List the toppings that are within the categories
        if user_topping in self.category_numbers:
            for key1, value1 in INGREDIENTS[user_topping].items():
                for num, item in enumerate(value1):
                    # Store the number of topping ↓↓↓↓
                    self.number_toppings_selected.append(num + 1)
                    # With this data I make the table ↓↓↓↓
                    oTtoppings.add_row([key1, num + 1, item.title()])
                    self.topping_names.append(item.title())

            print(oTtoppings)

        elif user_topping not in self.category_numbers:
            print("Selection must be a number from category. Try again.")
            self.is_On = False

    def selectTopping(self):
        """This method prints and stores the selected additions."""

        clear_cmd = 'os.system("clear")'

        oTselection = PrettyTable()
        oTselection.field_names = ["Custom Pizza Order"]

        self.back_off = input("Do you want to select an option? Press 'y' or 'n': ").lower()
        if self.back_off == 'n':
            exec(clear_cmd)
        elif self.back_off == 'y':
            number_selection = int(input("Write the number of your choice: "))
            exec(clear_cmd)
            if number_selection in self.number_toppings_selected:
                index_selected = number_selection - 1
                selection = self.topping_names[index_selected]
                self.topping_selected.append(selection)
                self.addtion_counter += 1
            else:
                print('')
                print("WRONG TYPING. TRY AGAIN.")
                self.is_On = False

            # Create a table of table of toppings selected
            if self.addtion_counter == self.maximum_toppings:
                for item in self.topping_selected:
                    oTselection.add_row([item])
                print("<====== Here is your Custom Pizza ======>")
                print(oTselection)
                self.is_On = False
            elif self.addtion_counter != self.maximum_toppings:
                print(f"You have selected ===> {self.addtion_counter} Toppings")
                print("Topping Selected ===> ", ', ' .join(self.topping_selected))
        else:
            print('')
            print("WRONG TYPING. TRY AGAIN.")
            self.is_On = False

    def builtApizza(self):
        """This method counts the toppings I select to build the pizza.
        The maximum number of toppings that I can select is 4.
        If I want to change this number I can do it from the attribute (self.maximum_toppings)"""

        while self.is_On:
            self.showToppings()
            self.availableToppings()
            self.selectTopping()


    def payment(self, amount):
        
        try:
            amount = float(amount)
            if amount >= 0:
                return True
            else:
                return False
        except ValueError:
            return False


if __name__ == "__main__":
    # Create Object from the class Custompizza
    oCustompizza = Custompizza()

    # Call methods from the oCustompizza
    oCustompizza.builtApizza()
