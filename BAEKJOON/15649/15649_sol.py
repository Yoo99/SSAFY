import sys
sys.stdin = open("input.txt")

from itertools import permutations

N, M  = map(int, input().split())
numbers = [i for i in range(1, N+1)]
for item  in list(permutations(numbers, M)):
    for d in item:
        print(d, end=  ' ')
    print()