from menu import MENU
from prettytable import PrettyTable


# Presetpizza class
class Presetpizzas:
    """This class is developed to work based on the 'menu.py' file 
    that contains the 'MENU' variable, which is a dictionary with pre-established pizzas.
    Without this file (menu.py) this class will not work correctly."""

    def __init__(self):
        self.category_letter = ''
        self.number_selection = 0
        self.category_names = ''
        self.pizza_numbers = []
        self.pizza_names = []
        self.ingredients = []
        self.prices = []
        self.orderStore = {}

    def listPresetCategories(self):
        """This method return the list of preset categories"""

        oTable = PrettyTable()
        oTable.field_names = ["Letter", "Categories"]

        categoryNames = []
        for key1, value1 in MENU.items():
            for key2, value2 in value1.items():
                oTable.add_row([key1, key2])
                categoryNames.append(key2)

        print(oTable)

    def defaultPizza(self):
        """This method return a table of pizza menu so that you can explore 
        the entire catalog it is advisable to use this method within a while loop"""

        oTable2 = PrettyTable()
        oTable2.field_names = ["Category", "Number", "Pizza Names", "Ingredients", "price"]

        # User's letter - Selection of the Category
        self.category_letter = input("Select the category by writing the letter: ")

        for key1, value1 in MENU[self.category_letter].items():
            self.category_names = key1
            for key2, value2 in value1.items():
                self.pizza_numbers.append(key2)
                for key3, value3 in value2.items():
                    self.pizza_names.append(key3)
                    for key4, value4 in value3.items():
                        if key4 == "Ingredients":
                            self.ingredients.append(value4)
                        if key4 == "price":
                            self.prices.append(value4)

        # Convert nested list (self.ingredients) to lowercase to save space in the table
        self.ingredients = [[str(item_).lower()for item_ in sub_list]
                            for sub_list in self.ingredients]

        category = self.category_names
        for item in range(0, len(self.pizza_numbers)):
            numbers = self.pizza_numbers[item]
            names = self.pizza_names[item]
            ingredients = self.ingredients[item]
            price = self.prices[item]

            oTable2.add_row([category, numbers, names, ',' .join(ingredients), price])

        return oTable2

    def defaultOrder(self):
        """This method prints the result of my final order and along 
        with it stores in a variable called 'self.orderStore' a dictionary 
        with the order data."""

        oTotalt = PrettyTable()
        oTotalt.field_names = ["Pizza Selected", "Ingredients", "Total"]

        self.number_selection = int(input("Choose the number of pizza you want: "))
        number_selected = self.number_selection - 1

        pizzaName = self.pizza_names[number_selected]
        pizza_ingredients = self.ingredients[number_selected]
        price = self.prices[number_selected]

        if self.number_selection in self.pizza_numbers:
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


if __name__ == "__main__":

    # Create the Object "oPresetPizza"
    oPresetPizza = Presetpizzas()

    # Call methods from the Object (oPresetPizza)
    oPresetPizza.listPresetCategories()
    print(oPresetPizza.defaultPizza())
    oPresetPizza.defaultOrder()
    print(oPresetPizza.orderStore)

    print("")
    print("This is the class Presetpizza")
