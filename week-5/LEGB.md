## What would be the output of this program?


def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)





# Output:
a = 30 
a = 20
a = 10
