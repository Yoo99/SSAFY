import sys
sys.stdin = open("input.txt")

from itertools import product
n = int(input())
numbers= [i for i in range(1, 10)]
cnt  = 0
for item in list(product(numbers, repeat = n)):
    flag = True
    for d in range(0, len(item)-1):
        diff = abs(item[d] - item[d+1])
        if diff <=2:
            continue
        else:
            flag = False
            break
    if flag:
        cnt +=1
    else:
        continue
print(cnt)
