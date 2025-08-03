import sys
sys.stdin = open("input.txt")
from collections import  deque, defaultdict

n = int(input())
q = defaultdict(list)
temp = deque()
for _ in range(n):
    line=  list(map(int, input().split()))
    if len(line) ==2:
        temp.append(line[1])
        q[len(temp)].append(temp[-1])
    else:
        temp.popleft()
max_cnt = 0
for key in q.keys():
    if key>max_cnt:
        max_cnt = key
min_ans = 100000
for d in q[max_cnt]:
    if d<min_ans:
        min_ans =d
print(max_cnt, min_ans)
