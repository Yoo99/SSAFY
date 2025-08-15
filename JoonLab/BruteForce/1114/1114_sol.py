import sys
sys.stdin = open("input.txt")

from itertools import combinations

words = str(input()).strip()
k = int(input())

answer = []
d = list(combinations(words, k))
print(d)
for ele in d:
    answer.append(ele)
answer.sort()
for item in answer:
    print(''.join(item))