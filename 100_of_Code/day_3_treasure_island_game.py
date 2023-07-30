print('*******************************************************************************')
print('          |                   |                  |                     |')
print(' _________|________________.=""_;=.______________|_____________________|_______')
print('|                   |  ,-"_,=""     `"=.|                  |')
print('|___________________|__"=._o`"-._        `"=.______________|___________________')
print('          |                `"=._o`"=._      _`"=._                     |')
print(' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______')
print('|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |')
print('|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________')
print('          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |')
print(' _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______')
print('|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |')
print('|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________')
print('____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____')
print('/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_')
print('____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____')
print('/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_')
print('____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____')
print('/______/______/______/______/______/______/______/______/______/______/_____ /')
print('*******************************************************************************\n')

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure')

answer_1 = input('You\'re at a cros road. Where do you want to go? Type "left" or "right"\n')

if answer_1 == 'left':
  answer_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if answer_2 == 'wait':
    answer_3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
    if answer_3 == 'red':
      print('It is a room full of fire. Game Over.')
    elif answer_3 == 'blue':
      print('You enter a room of beasts. Game Over.')
    elif answer_3 == 'yellow':
      print('You found the treasure! You Win!')
    else:
        print('You choose a door that doesn\'t exist')
  else:
    print('You get attacked by an angry trout. Game Over.')
else:  
  print('You fell into a hole. Game Over')
