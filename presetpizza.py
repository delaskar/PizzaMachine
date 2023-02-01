from menu import MENU
from prettytable import PrettyTable


# Presetpizza
class Presetpizzas:

    def __init__(self):
        self.category_letter = ''
        self.number_selection = 0
        self.category_names = ''
        self.pizza_numbers = []
        self.pizza_names = []
        self.ingredients = []
        self.prices = []


    def listPresetCategories(self):
        """This method return the list of preset categories"""
        
        table = PrettyTable()
        table.field_names = ["Letter", "Categories"]        

        categoryNames = []
        for key1, value1 in MENU.items():
            for key2, value2 in value1.items():
                table.add_row([key1, key2])
                categoryNames.append(key2)
        
        print(table)


    def defaultPizza(self):
        """This method return a table of pizza menu so that you can explore 
        the entire catalog it is advisable to use this method within a while loop"""

        table2 = PrettyTable()
        table2.field_names = ["Category", "Number", "Pizza Names", "Ingredients", "price"]

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
        result_sub_list = [[str(item_).lower()for item_ in sub_list]for sub_list in self.ingredients]
        
        category = self.category_names
        for item in range(0, len(self.pizza_numbers)):
            numbers = self.pizza_numbers[item]
            names = self.pizza_names[item]
            ingredients = result_sub_list[item]
            price = self.prices[item]

            table2.add_row([category, numbers, names, ',' .join(ingredients), price])
        
        return table2





if __name__ == "__main__":
    
    # Create the Object "oPresetPizza"
    oPresetPizza = Presetpizzas()

    # Call methods from the Object (oPresetPizza)
    oPresetPizza.listPresetCategories()
    print(oPresetPizza.defaultPizza())

    print("This is the class Presetpizza")
