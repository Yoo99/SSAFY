import sys
from itertools import combinations, permutations

sys.stdin = open("input.txt")

N = int(input())
maze = []
for _ in range(N):
    line = list(map(int, input().split()))
    maze.append(line)
iter = [i for i in range(N)]
flag = True
min_diff = 1000000000000
for d in combinations(iter,N//2):
    if not flag:
        break
    start = list(d)
    r = list(set(iter) - set(d))
    comb_start = list(combinations(start, 2))
    rest_start = list(combinations(r, 2))
    start_sum, rest_sum = 0, 0
    for ele in comb_start:
        i, e = ele[0], ele[1]
        start_sum +=(maze[i][e] +maze[e][i])
    for ele in rest_start:
        i, e = ele[0], ele[1]
        rest_sum +=(maze[i][e] + maze[e][i])
    diff = abs(start_sum - rest_sum)
    if diff ==0:
        min_diff = 0
        flag = False
        break
    elif diff<min_diff:
        min_diff = diff
    else:continue
print(min_diff)
