import sys
sys.stdin = open("5607_input.txt")
def combination(n, r):
    dp = [[0] * (r + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
        for j in range(1, min(i, r) + 1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][r]

T = int(input())
for test_case in range(1, T+1):
    n, r = map(int, input().split())
    print(f"#{test_case} {combination(n, r)}")
