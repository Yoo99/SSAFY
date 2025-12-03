import sys
sys.stdin = open("input.txt")

import bisect
n, m = map(int, input().split())
arr = list(map(int ,input().split()))
for _ in range(m):
    i, j = map(int, input().split())