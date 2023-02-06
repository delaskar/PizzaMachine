from custompizza import Custompizza
from presetpizza import Presetpizzas
from art import *


oCustompizza = Custompizza()
oPresetpizza = Presetpizzas()

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


while True:
        user_prompt = input("What do you want to order?. Type the number: ")
        if user_prompt.isdigit():
            break
        else:
            print("Selection must be a number. Try again.")

user_prompt = int(user_prompt)
if user_prompt == 1:
     oCustompizza.builtApizza()

elif user_prompt == 2:
     oPresetpizza.builtApresetPizza()

else:
     print("WRONG TYPING. TRY AGAIN")
     