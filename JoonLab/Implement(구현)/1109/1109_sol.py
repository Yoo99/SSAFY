import sys
sys.stdin = open("input.txt")

from itertools import permutations
arr = list(input())
ans = []
for ele in permutations(arr):
    d = ''.join(ele)
    ans.append(d)
ans.sort()
for answer in ans:
    print(answer)
