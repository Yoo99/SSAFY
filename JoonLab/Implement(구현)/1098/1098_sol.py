import sys
sys.stdin = open("input.txt")

_, m = map(int,input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    q = list(map(int, input().split()))
    if len(q)==3:
        i,j = q[1], q[2]
        print(sum(arr[i:j+1]))
    else:
        s,e,k = q[1],q[2],q[3]
        for d in range(s, e+1):
            arr[d] +=k
