#Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters.

def upperlower(letters):
    upper = 0
    lower = 0

    for i in letters:
        if (i.isupper()) == True:
            upper += 1
        elif (i.islower()) == True:
            lower += 1
    print("sum of uppercase letters = ", +upper)
    print("sum of lowercase letters = ", +lower)



print(upperlower(input("Enter string: ")))