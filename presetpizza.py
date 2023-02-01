from menu import MENU
from prettytable import PrettyTable


# Presetpizza
class Presetpizzas:

    def __init__(self):
        self.category_letter = ''
        self.category_names = []
        self.pizza_names = []
        self.ingredients = []
        self.price = []


    def listPresetCategories(self):
        """This method return the list of preset categories"""
        
        table = PrettyTable()
        table.field_names = ["Letter", "Categories"]        

        for key1, value1 in MENU.items():
            for key2, value2 in value1.items():
                table.add_row([key1, key2])
                self.category_names.append(key2)
        
        print(table)


    def defaultPizza(self):
        """This method return a table of pizza menu"""

        table2 = PrettyTable()
        table2.field_names = ["Category", "Number", "Pizza Names", "Ingredients", "price"]

        # self.category_letter = input("Select the category by writing the letter: ")
        font_size = 5
        for key1, value1 in MENU["b"].items():
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    for key4, value4 in value3.items():
                        if key4 == "Ingredients":
                            price = MENU['b'][key1][key2][key3]["price"]
                            for item in value4:
                                table2.add_row([key1, key2, key3, item, price])      


        table2.align["Ingredients"] = "l"
        print(table2)


if __name__ == "__main__":
    # Create the Object "oPresetPizza"
    oPresetPizza = Presetpizzas()

    # Call method from the Object (oPresetPizza)
    # oPresetPizza.listPresetCategories()
    oPresetPizza.defaultPizza()
    print("This is the class Presetpizza")
