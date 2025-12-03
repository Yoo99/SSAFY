import sys
sys.stdin = open("input.txt")

import bisect

n, m = map(int,input().split())
arr=  list(map(int, input().split()))
arr.sort()
for _ in range(m):
    num = int(input())
    d = bisect.bisect_right(arr, num)
    print(n-d)
