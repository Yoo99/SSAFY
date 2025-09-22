import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
prefix = [0 for _ in range(N+1)]
arr = list(map(int, input().split()))
for i in range(N):
    prefix[i+1] += arr[i]
    prefix[i+1] += prefix[i]
for _ in range(M):
    s,e = map(int, input().split())
    print(prefix[e] - prefix[s-1])