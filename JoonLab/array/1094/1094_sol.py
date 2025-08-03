import sys
sys.stdin = open("input.txt")

from collections import deque


n = int(input())
temp = deque()
A = [] # 원하는 메뉴를 먹은 경우
B = [] # 원하지 않는 메뉴를 먹은 경우
C = [] # 먹지 못한 경우
for _ in range(n):
    line = list(map(int,input().split()))
    if line[0] ==1:
        temp.append((line[1], line[2]))
    elif line[0] == 2:
        num, menu=  temp.popleft()
        if line[1]==menu:
            A.append(num)
        else:
            B.append(num)
if temp:
    for item in temp:
        C.append(item[0])
A.sort()
B.sort()
C.sort()
if len(A)==0:
    print("None")
else:
    for d in A:
        print(d, end = ' ')
    print()
if len(B)==0:
    print("None")
else:
    for b in B:
        print(b, end = ' ')
    print()
if len(C)==0:
    print("None")
else:
    for c in C:
        print(c, end = ' ')
    print()