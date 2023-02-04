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
        self.add_topping_counter = 0
        self.maximum_number_additions = 4
        self.number_toppings_selected = []  # Store the options of toppings
        self.toppings_selected = []  # Store the name of toppings
        self.number_of_order = 0
        self.maximun_order = 0
        self.counter_order = 0
        self.total = 0


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


    def toppings(self):

        clear_cmd = 'os.system("clear")'

        while True:
            user_order = input("How many pizza orders do you want?: ")
            if user_order.isdigit():
                break
            else:
                print("You must enter an integer. Try again")
        
        user_order = int(user_order)
        self.maximun_order = user_order
       
        while True:

            if self.counter_order <= self.maximun_order:
                # Call showToppingd
                self.showToppings()
            
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
                selections = []
                if user_topping in self.category_numbers:
                    for key1, value1 in INGREDIENTS[user_topping].items():
                        for num, item in enumerate(value1):
                            self.number_toppings_selected.append(num + 1)
                            oTtoppings.add_row([key1, num + 1, item.title()])
                            selections.append(item.title())
                else:
                    print("WRONG TYPING. TRY AGAIN.")
                    break

                print(oTtoppings)
                
                is_On = True
                while is_On:
                    if self.add_topping_counter <= self.maximum_number_additions:
                        back_off = input("Do you want to select an option? Press 'y' or 'n': ").lower()
                        if back_off == 'n':
                            exec(clear_cmd)
                            is_On = False
                        elif back_off == 'y':
                            number_selection = int(input("Write the number of your choice: "))
                            exec(clear_cmd)
                            if number_selection in self.number_toppings_selected:
                                index_selected = number_selection - 1
                                self.toppings_selected.append(selections[index_selected])
                                self.add_topping_counter += 1
                                print('')
                                print(f"The maximum number of toppings you can choose is: {self.maximum_number_additions * self.maximun_order}, four(4) for each pizza")
                                print("Number of toppings selected ===> ", self.add_topping_counter)
                                print("Topping Selected ===> ", ', ' .join(self.toppings_selected))
                                print('')
                                is_On = False
                            else:
                                print('')
                                print("WRONG TYPING. TRY AGAIN.")
                                break
                        else:
                            print('')
                            print("WRONG TYPING. TRY AGAIN.")
                            break
                    else:
                        print("")
                        print("=== You have reached your maximum number of toppings. ===")
                        is_On = False

                if self.add_topping_counter == self.maximum_number_additions:
                    self.counter_order += 1
                    print('')
                    print(f"Your number order is: {self.maximun_order}")
                    print(f"Your current order is: {self.counter_order}")
                    print('')
                else:
                    pass

            else:
                for item in self.maximun_order:
                    print("processing your order...")
                break



if __name__ == "__main__":

    oCustompizza = Custompizza()
    oCustompizza.toppings()
