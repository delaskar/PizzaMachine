from custompizza import Custompizza
from presetpizza import Presetpizzas
from welcome import user_welcome
import os

clear_cmd = 'os.system("clear")'

oCustompizza = Custompizza()
oPresetpizza = Presetpizzas()


ROUNNDS = 2
counter = 0

machine_On = True
while machine_On:

     if counter <= 2:

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
               
               user_amount1 = input("Enter the amount: $")
               oCustompizza.payment(user_amount1)
               

          elif user_prompt == 2:
               oPresetpizza.builtApresetPizza()
               
               user_amount2 = input("Enter the amount: $")
               oPresetpizza.payment(user_amount2)

          else:
               print("WRONG TYPING. TRY AGAIN")
          
          print('')
          user_question = input("Do you want to order a new pizza?: Press 'y' or 'n': ")

          if user_question == 'y':
               counter += 1
               exec(clear_cmd)
               pass
          else:
               machine_On = False

          if counter == 2:
               machine_On = False
