import sys
sys.stdin = open("2817_input.txt")


T  = int(input())
for test_case in range(1, T+1):
    N, K=  map(int, input().split())
    arr = list(map(int, input().split()))
    total = []
    subset_cnt = 2 ** len(arr)
    subsets = []
    for i in range(subset_cnt):
        subset = []
        for j in range(len(arr)):
            if i & (1<<j):
                subset.append(arr[j])
                print(subset)
        subsets.append(subset)
    print(subsets)
    count = 0
    for b in subsets:
        if sum(b) == K:
            count+=1
        else:
            continue
    print(f"#{test_case} {count}")