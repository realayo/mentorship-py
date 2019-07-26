def CheckNums(num1, num2):

    if num1 == num2:
        return - 1
    elif num2 > num1:
        return True
    else:

        return False


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print (CheckNums(num1, num2))