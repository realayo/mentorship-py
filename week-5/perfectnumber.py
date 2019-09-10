'''Write a Python function to check whether a number is perfect or not. '''

def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num, "is a perfect number")

    else:
        print(num, "is not a perfect number")

print(perfect_number(int(input("Enter a number: "))))
