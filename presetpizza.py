from menu import MENU
from prettytable import PrettyTable
import os


# Presetpizza class
class Presetpizzas:
    """This class is developed to work based on the 'menu.py' file 
    that contains the 'MENU' variable, which is a dictionary with pre-established pizzas.
    Without this file (menu.py) this class will not work correctly."""

    def __init__(self):
        self.category_letter = ''
        self.number_selection = 0
        self.category_names = ''
        self.list_letters_category = []
        self.pizza_numbers = []
        self.pizza_names = []
        self.ingredients = []
        self.prices = []
        self.orderStore = {}
        
        self.user_selection = ''
        self.On = True

    def listPresetCategories(self):
        """This method return the list of preset categories"""

        oTable = PrettyTable()
        oTable.field_names = ["Letter", "Categories"]

        categoryNames = []
        for key1, value1 in MENU.items():
            self.list_letters_category.append(key1)
            for key2, value2 in value1.items():
                oTable.add_row([key1, key2])
                categoryNames.append(key2)

        print(oTable)

    def defaultPizza(self):
        """This method return a table of pizza menu so that you can explore 
        the entire catalog it is advisable to use this method within a while loop"""

        clear_cmd = 'os.system("clear")'

        oTable2 = PrettyTable()
        oTable2.field_names = ["Category", "Number", "Pizza Names", "Ingredients", "price"]

        # User's letter - Selection of the Category
        self.category_letter = input("Select the category by writing the letter: ")
        if self.category_letter in self.list_letters_category:
            # Temporary variables
            _category_names = ''
            _pizza_numbers = []
            _pizza_names = []
            _ingredients = []
            _prices = []
            
            for key1, value1 in MENU[self.category_letter].items():
                _category_names = key1
                for key2, value2 in value1.items():
                    _pizza_numbers.append(key2)
                    for key3, value3 in value2.items():
                        _pizza_names.append(key3)
                        for key4, value4 in value3.items():
                            if key4 == "Ingredients":
                                _ingredients.append(value4)
                            if key4 == "price":
                                _prices.append(value4)

            # Convert nested list (self.ingredients) to lowercase to save space in the table
            _ingredients = [[str(item_).lower()for item_ in sub_list]
                                for sub_list in _ingredients]

            category = _category_names
            for item in range(0, len(_pizza_numbers)):
                numbers = _pizza_numbers[item]
                names = _pizza_names[item]
                ingredients = _ingredients[item]
                price = _prices[item]

                oTable2.add_row([category, numbers, names, ',' .join(ingredients), price])

            print(oTable2)
      
        
            self.user_selection = input("Do you want to select an option? Press 'y' or 'n': ")
            
            if self.user_selection == 'y':
                self.category_names = _category_names
                self.pizza_numbers = _pizza_numbers
                self.pizza_names = _pizza_names
                self.ingredients = _ingredients
                self.prices = _prices
                pass

        else:
            print("WRONG TYPING. TRY AGAIN")
            exec(clear_cmd)


    def defaultOrder(self):
        """This method prints the result of my final order and along 
        with it stores in a variable called 'self.orderStore' a dictionary 
        with the order data."""

        clear_cmd = 'os.system("clear")'

        oTotalt = PrettyTable()
        oTotalt.field_names = ["Pizza Selected", "Ingredients", "Total"]

        
        if self.user_selection == 'y':

            try:
                # Check if the user input is a number from the Toppings category
                while True:
                    self.number_selection = input("Choose the number of pizza you want: ")
                    if self.number_selection.isdigit():
                        break
                    else:
                        print("Selection must be a number from category. Try again.")
                
                number_selected = int(self.number_selection) - 1

                pizzaName = self.pizza_names[number_selected]
                pizza_ingredients = self.ingredients[number_selected]
                price = self.prices[number_selected]
            
            except IndexError:
                print("Selection must be a number from list.")

            if int(self.number_selection) in self.pizza_numbers:
                pizzaIngredients = ',' .join(pizza_ingredients)
                oTotalt.add_row([pizzaName, pizzaIngredients, price])

                # Created a Dictionary as a new attribute to store the order and later be able to loop while
                self.orderStore['pizza'] = pizzaName
                self.orderStore['ingredient'] = pizzaIngredients
                self.orderStore['price'] = price

                print("")
                print("↓↓↓ Here is your order and the total to pay. ↓↓↓")
                print("")
                print(oTotalt)
                print("")
                self.On = False
            else:
                print("WRONG TYPING. TRY AGAIN")
                self.On = False

        elif self.user_selection == 'n':
            exec(clear_cmd)
            pass

        else:
            print("WRONG TYPING. TRY AGAIN")



    def builtApresetPizza(self):
        """This method processes the pizza"""

        while self.On:
            self.listPresetCategories()
            self.defaultPizza()
            self.defaultOrder()


    def is_valid_amount(self, amount):
        """This metho verify is the amount is valid"""

        try:
            amount = float(amount)
            if amount >= 0:
                return True
            else:
                return False
        except ValueError:
            return False


    def payment(self, amount):
            """This method makes the payment"""
            
            if self.is_valid_amount(amount):
                amount = float(amount)
                if amount > self.orderStore['price']:
                    result = amount - self.orderStore['price']
                    print(f"Thank you for your purchese!\nHere is your remain: ${result}")
                    print("Enjoy you pizza!")
                elif amount < self.orderStore['price']:
                    print(f"Your amount: ${amount} is not enough.")
                elif amount == self.orderStore['price']:
                    print("Thank your for your purchese!")
                    print("Enjoy your pizza!")
            else:
                print("The amount is invalid")


if __name__ == "__main__":
    # Create the Object "oPresetPizza"
    oPresetPizza = Presetpizzas()

    # Call methods from the Object (oPresetPizza)
    oPresetPizza.builtApresetPizza()

    print("")
    print("This is the class Presetpizza")
