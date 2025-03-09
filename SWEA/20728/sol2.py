import sys
sys.stdin = open("20728_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    diff = max(arr)-min(arr)
    for i in range(0, len(arr)-K+1):
        subset = arr[i:i+K]
        if max(subset)-min(subset)<diff:
            diff = max(subset)-min(subset)
    print(f'#{test_case} {diff}')