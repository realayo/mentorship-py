import random
print(random.randint(1, 6))
while True:
    roll = random.randint(1, 6)
    roll_again = input("To roll again, enter (y/n): ")
    while roll_again != "y":
        if roll_again == "n":
            print("Game Over")
            quit()
        else:
            print("Invalid input")
            roll_again = input("Roll again? (y/n)")
    if roll_again == "y":
        print(roll)
    elif roll_again == "n":
        quit()