import sys
sys.stdin = open("1764_input.txt")

while True:
    try:
        N, M = map(int, input().split())
        heard = list()
        for _ in range(N):
            heard.append(input())
        seen = list()
        for _ in range(M):
            seen.append(input())
        ans = []
        if N > M:
            long, short = set(heard), set(seen)
        else:
            long, short =set(seen), set(heard)
        for b in long:
            if b in short:
                ans.append(b)
        ans.sort()
        print(len(ans))
        for ele in ans:
            print(ele)
    except:
        break