from custompizza import Custompizza
from presetpizza import Presetpizzas
from art import *
import os

clear_cmd = 'os.system("clear")'

oCustompizza = Custompizza()
oPresetpizza = Presetpizzas()

def user_welcome():
     """This function prints the welcome"""

     print("")
     print("")
     print("                 <======↓↓↓ Welcome To ↓↓↓======>")
     tprint("Pizza Machine")
     print("         <>======<><>======<><>======<><>======<><>======<>")
     print("")
     print("")

     print("To order your pizza you can choose between the two options we have:")
     print("")
     print("1. Order a Custom Pizza")
     print("2. Order a Prepackaged Pizza")
     print("")
     print("NOTE:\n      All CUSTOM PIZZAS have a value of: $15 per pizza.")
     print("")

machine_On = True
while machine_On:

     user_welcome()

     while True:
          user_prompt = input("What do you want to order?. Type the number: ")
          if user_prompt.isdigit():
               break
          else:
               print("Selection must be a number. Try again.")

     user_prompt = int(user_prompt)
     if user_prompt == 1:
          oCustompizza.builtApizza()
          
          user_amount1 = input("Enter the amount:")
          oCustompizza.payment(user_amount1)
          

     elif user_prompt == 2:
          oPresetpizza.builtApresetPizza()
          
          user_amount2 = input("Enter the amount:")
          oPresetpizza.payment(user_amount2)

     else:
          print("WRONG TYPING. TRY AGAIN")
     
     print('')
     user_question = input("Do you want to order a new pizza?: ")

     if user_question == 'y':
          exec(clear_cmd)
          pass
     else:
          machine_On = False
