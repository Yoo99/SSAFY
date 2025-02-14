import sys
from itertools import combinations
sys.stdin = open('1486_input.txt')

T = int(input())
for test_case in range(1, T+1):
# N명, B 높이의 선반
    N, B = map(int, input().split())
    height=  list(map(int, input().split()))
    comb = []
    for i in range(1, len(height)+1):
        arr = list(combinations(height,i))
        comb.extend(arr)
    ans = []
    for b in comb:
        if sum(b)>=B:
            ans.append(sum(b))
    print(f"#{test_case} {min(ans)-B}")