from menu import MENU
from prettytable import PrettyTable

# Presetpizza
class Presetpizzas:

    def __init__(self, category_letter):
        self.category_letter = category_letter
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
        
        print(table)


if __name__ == "__main__":
    oPresetPizza = Presetpizzas("test")
    oPresetPizza.listPresetCategories()
    print("This is the class Presetpizza")
