# Given: Two positive integers a<b<10000
# Return: The sum of all odd integers from a through b inclusively. (Solve using for loops and while loops
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

def sumofodd(a,b):

    value = 0
    while a < b < 10000:
        for i in range(int(a), int(b)+1):
            if i % 2 != 0:
                value += i
        return value

    if int(a) > 10000 or int(b) > 10000:
        print("Please enter a valid number")

    elif int(a) == 0 or int(b) == 0:
        print("Enter a number greater than 0")

    elif int(a) > int(b):
        print("The 1st number can't be greater than the 2nd number")

    else:
        print("Please enter valid numbers")


print(sumofodd(int(input("Enter 1st number: ")), int(input("Enter 2nd number: "))))




