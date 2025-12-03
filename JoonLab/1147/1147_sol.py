import sys
sys.stdin = open("input.txt")

n,m = map(int, input().split())
arr = list(map(int, input().split()))
t = [0 for _ in range(n)]
prefix = [0 for _ in range(n+1)]
flag = False
for _ in range(m):
    line = list(map(int, input().split()))
    if line[0] == 1:
        s,e = line[1], line[2]
        t[s] += line[3]
        if (e+1)< n:
            t[e+1] -= line[3]
    else:
        if not flag:
            flag = True
            for i in range(1, n):
                t[i] += t[i-1]
            for i in range(n):
                arr[i] = arr[i] + t[i]
            for i in range(1, n+1):
                prefix[i] += (prefix[i-1] + arr[i-1])
        s,e = line[1],line[2]
        print(prefix[e+1] - prefix[s])
