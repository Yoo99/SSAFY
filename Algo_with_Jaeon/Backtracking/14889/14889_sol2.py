import sys
sys.stdin = open("14889_input.txt")
from itertools import combinations

N = int(input())
num_list = [i for i in range(N)]
d = set(combinations(num_list, N//2))
arr = [list(map(int,input().split())) for _ in range(N)]
min_diff = float('inf')
for ele in d:
    team_a, team_b = 0 , 0
    print(ele)
    for e in set(combinations(ele,2)):
        team_a += arr[e[0]][e[1]]
    rest = set(num_list) - set(ele)
    for f in set(combinations(rest, 2)):
        print(f)
        team_b += arr[f[0]][f[1]]
    print(team_a, team_b)
    diff = abs(team_a - team_b)
    print(diff)
    if diff < min_diff:
        min_diff = diff
    if min_diff ==0:
        break
print(min_diff)