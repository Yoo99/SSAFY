import sys
sys.stdin = open("input.txt")

import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(m):
    num = int(input())
    print(n-bisect.bisect_left(arr, num))