def KFC(num):
    if num==3:
        return
    print(num)
    KFC(num +1)
    KFC(num + 1)
    print(num, end= ' ')
KFC(0)
print("끝")