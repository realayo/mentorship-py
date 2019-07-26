def timeconvert(num):
    hour = num // 60
    minute = num % 60

    return "{} hour(s) {} minutes".format(hour, minute)

num = int(input("Enter a number to convert: "))
if num < 0:
    print ("Invalid operation, enter a positive number")
else:
    print (timeconvert(num))