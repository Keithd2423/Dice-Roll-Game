

#creating a dice roll game that makes a player roll a dice vs a computer. Then selects a winner based on a higher number.
greeting = input("would you like to roll the dice? [Y/N]").lower()

import random

computer_roll = random.randint(1, 10)

player_roll = random.randint(1,10)

if (greeting == "y"):
    print("Your random number is:", player_roll)

elif (greeting == "n"):
    print("Program ended")


computer_roll = random.randint(1, 10)
print("Computer rolled:", computer_roll)

if computer_roll > player_roll:
    print("The computer wins!")

if computer_roll < player_roll:
    print("You Win!")



#storing computer and player diceroll

#Using logic to choose a winner
#printing results
