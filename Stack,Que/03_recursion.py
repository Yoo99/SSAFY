def fact(item):
    if item ==1:
        return 1
    else:
        return item * fact(item-1)

print(fact(4))