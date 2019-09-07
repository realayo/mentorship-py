def firstreverse(str):
    new_str = ''
    n = len(str)
    while n:
        n -= 1
        new_str += str[n]
    return new_str

print (firstreverse(input("Enter a word: ")))