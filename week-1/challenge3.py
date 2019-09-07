def FirstFactorial(num):
    if num == 1:
        return num
    else:
        return num * FirstFactorial(num - 1)


num = int(input("Enter a number: "))
if num < 0:
    print("sorry, factorial is not possible on negative numbers")
elif num == 0:
    print("0 factorial is 1")
else:
    print (FirstFactorial(num))