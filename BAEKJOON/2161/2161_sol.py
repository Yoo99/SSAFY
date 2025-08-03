import sys
sys.stdin = open("input.txt")
from collections import deque
N = int(input())
arr = deque(i for i in range(1, N+1))
ans = []
for _ in range(N-1):
    first = arr.popleft()
    ans.append(first)
    d = arr.popleft()
    arr = arr + deque([d])
last = arr.popleft()
ans.append(last)
answer = ''
for d in ans:
    answer += str(d)+ " "
print(answer.rstrip())