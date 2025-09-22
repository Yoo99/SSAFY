import sys
sys.stdin = open("input.txt")

N , M = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]
for _ in range(M-1):
    _, i, j, k = map(int, input().split())
    prefix[i] += k
    if j+1 <= N-1:
        prefix[j+1] -= k

add = 0
for idx in range(N):
    add += prefix[idx]
    arr[idx] += add
S = [0 for _ in range(N+1)]
for d in range(N):
    S[d+1] = S[d] + arr[d]
_, i, j  = map(int, input().split())
print(S[j+1] -S[i])

