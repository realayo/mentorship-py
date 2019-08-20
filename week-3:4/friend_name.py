def friends_list(names):
    new_names = []

    for i in names:
        if len(i) == 4:
            new_names.append(i)
    return new_names




names = (input("Enter friends' name separated by a comma: ")).split(",")
print(friends_list(names))