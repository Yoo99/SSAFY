import sys
sys.stdin = open("20728_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K=  map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = float('inf')
    for i in range(N-K+1):
        diff = arr[K-1+i] - arr[i]
        if diff < ans:
            ans = diff
        else:
            continue
    print(f"#{test_case} {ans}")