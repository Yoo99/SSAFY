import sys
sys.stdin = open("input.txt")

from itertools import product
n = int(input())
path = []
total = 0
def recur(cnt):
    global total
    if cnt ==n:
        flag = True

        for d in range(0, len(path)-1):
            if abs(path[d] - path[d+1])>2:
                flag = False
                break
        if flag:
            # print(*path)
            total +=1
        return
    for num in range(1, 10):
        path.append(num)
        recur(cnt+1)
        path.pop()

recur(0)
print(total)
