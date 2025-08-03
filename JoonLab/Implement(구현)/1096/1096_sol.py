import sys
sys.stdin = open("input.txt")

_, m=  map(int, input().split())
arr = list(map(str, input().split()))
for _ in range(m):
    d = str(input()).rstrip()
    if d != '-':
        print(arr.count(d))
    else:
        print(len(arr))
