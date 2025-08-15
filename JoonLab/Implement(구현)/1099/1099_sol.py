import sys
sys.stdin = open("input.txt")

n, m =  map(int, input().split())
arr = []
for _ in range(n):
    line=  list(map(int, input().split()))
    arr.append(line)
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0]==1:
        for idx in range(q[1], q[3]+1):
            for idy in range(q[2], q[4]+1):
                arr[idx][idy] +=q[5]
    else:
        cnt =0
        for idx in range(q[1], q[3]+1):
            for idy in range(q[2], q[4]+1):
                cnt += arr[idx][idy]
        print(cnt)