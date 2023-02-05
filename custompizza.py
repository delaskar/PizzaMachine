from menu import INGREDIENTS
from prettytable import PrettyTable
import os


class Abortorder(Exception):
    """raise this exeption to abort the order."""
    pass


class Custompizza:
    
    def __init__(self):
        self.size = [6, 8]
        self.category_numbers = []
        self.number_toppings_selected = []  # Store the options of toppings
        self.topping_names = []  # Store the name of toppings
        self.topping_selected = []


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
                print("Selection must be a number from category. Try again")

        # converting the user input to an integer
        user_topping = int(user_topping)

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

        else:
            print("WRONG TYPING. TRY AGAIN.")


        
        
    def selectTopping(self):

        clear_cmd = 'os.system("clear")'

        back_off = input("Do you want to select an option? Press 'y' or 'n': ").lower()
        if back_off == 'n':
            pass
            # exec(clear_cmd)
        elif back_off == 'y':
            number_selection = int(input("Write the number of your choice: "))
            # exec(clear_cmd)
            if number_selection in self.number_toppings_selected:
                index_selected = number_selection - 1
                selection = self.topping_names[index_selected]
                self.topping_selected.append(selection)

                print('')
                print("Topping Selected ===> ", ', ' .join(self.topping_selected))
                print('')
            else:
                print('')
                print("WRONG TYPING. TRY AGAIN.")
        else:
            print('')
            print("WRONG TYPING. TRY AGAIN.")




if __name__ == "__main__":

    # Create Object from the class Custompizza
    oCustompizza = Custompizza()

    # Call methods from the oCustompizza
    oCustompizza.showToppings()
    oCustompizza.availableToppings()
    oCustompizza.selectTopping()
