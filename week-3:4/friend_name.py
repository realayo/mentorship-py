#Make a program that filters a list of strings and returns a list with only your friends names in it. If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure it’s not…
#Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friends_list(names):
    new_names = []

    for i in names:
        if len(i) == 4:
            new_names.append(i)
    return new_names


names = (input("Enter friends' name separated by a comma: ")).split(",")
print(friends_list(names))
