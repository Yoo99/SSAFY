import sys
sys.stdin = open("input.txt")

N = int(input())
T = [0] * (N)
P = [0] * (N)
for d in range(0, N):
    x,y = map(int, input().split())
    T[d] = x
    P[d] = y
answer = 0

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
print(dp[0])

