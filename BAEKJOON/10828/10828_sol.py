import sys
sys.stdin = open("10828_input.txt")
from collections import deque

N = int(input())
stack = deque([])
for _ in range(N):
    order = list(input().split())
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            d = stack.pop()
            print(d)