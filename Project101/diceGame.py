import random

response = "y"

while response == "y":
    dice_roll = random.randint(1, 6)

    print("---------")
    print("|       |")
    
    if dice_roll == 1:
        print("|   o   |")
    elif dice_roll == 2:
        print("| o   o |")
    elif dice_roll == 3:
        print("| o o o |")
    elif dice_roll == 4:
        print("| o o o |")
        print("| o o o |")
    elif dice_roll == 5:
        print("| o o o |")
        print("| o   o |")
    else:
        print("| o o o |")
        print("| o o o |")
        print("| o o o |")
    
    print("|       |")
    print("---------")

    response = input("Do you want to roll the dice again (y/n): ").lower()
