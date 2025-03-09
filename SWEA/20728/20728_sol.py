import sys
sys.stdin = open("20728_input.txt")
from itertools import combinations

T = int(input())
for test_case in range(1, T+1):
    N,K=  map(int, input().split())
    arr = list(map(int, input().split()))
    diff = []
    n = len(arr)
    subsets = list(combinations(arr, K))
    # for i in range(1<<n):
    #     subset = []
    #     for j in range(n):
    #         if i & (1<<j):
    #             subset.append(arr[j])
    #     subsets.append(subset)
    for ele in subsets:
        if len(ele)==K:
            max_ele = max(ele)
            min_ele = min(ele)
            diff.append(abs(max_ele - min_ele))
    print(f"#{test_case} {min(diff)}")