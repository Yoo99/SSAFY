import sys
sys.stdin = open("14889_input.txt")
from itertools import combinations


def rest_team(rest1, team_a):
    global min_diff
    rest_team  = set(combinations(rest1,2))
    print(rest_team)
    for b,e in rest_team:
        team_b = arr[b][e] + arr[e][b]
        print(team_b)
        if abs(team_a  - team_b)<min_diff:
            min_diff = abs(team_a - team_b)
        elif abs(team_a - team_b) == 0:
            min_diff = 0
            return min_diff

    return min_diff

N = int(input())# 한 변의 길이
mid = (N-2)//2  # 중간 부분
min_diff = float('inf')
num_list = set(i for i in range(N))

arr = [list(map(int, input().split())) for _ in range(N)]
print("mid", mid)
for i in range(mid+1):
    rest = num_list -{i}
    if min_diff == 0:
        break
    for j in rest:
        team_a  = arr[i][j] + arr[j][i]
        rest1 = rest - {j}
        print("team_a",i,j, team_a)
        print(rest_team(rest1, team_a))
        if min_diff !=0:
            continue
        else:
            break
print(min_diff)