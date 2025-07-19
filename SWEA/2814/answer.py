import sys
sys.stdin = open("2814_input.txt")

def dfs(c,v):
    global ans
    ans = max(ans,len(v)) # 최대값 갱신

    for n in adjL[c]:
        if n not in v:
            dfs(n,v+[n])

T = int(input())
for test_case in range(1,  T+1):
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e = map(int, input().split())
        adjL[s].append(e)
        adjL[e].append(s)

    ans = 0
    for s in range(1, N+1):
        dfs(s, [s])

print(ans)
