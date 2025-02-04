import sys
from itertools import combinations
sys.stdin = open("4012_input.txt", "r")

# tc = int(input())


tc=1
for test_case in range(1, tc+1):
    N = int(input())
    num = [i for i in range(1, N+1)]
    count = N//2
    comb = list(combinations((num), count))
    arr = []
    sum_arr = []
    comb_list = []
    for i in range(N):
        line= list(map(int, input().split()))
        arr.append(line)
    while comb:
        l1 = arr.pop(0)
        for b in comb:
            new_l = l1 + list(b)
            if len(set(new_l))==N:
                print(l1, b)
                # d1 = arr[i-1][j-1]
                # d2 = arr[j-1][i-1]
                # sum_1 = d1+d2
                # d3 = arr[b[0]-1][b[1]-1]
                # d4 = arr[b[1]-1][b[0]-1]
                # sum_2 = d3+d4
                # sum_arr.append(abs(sum_1 - sum_2))
            else:
                continue
    print(comb_list)
    print(min(sum_arr))