import sys
sys.stdin = open("4803_input.txt")
from collections import deque

def find_cycle(start):
    flag = False
    q = deque()
    q.append(start)


case = 1
while True:
    n, m = map(int, input().split())
    if n==0 and m == 0:
        break
    graph = {key: [] for key in range(1, n+1)}
    visited = [0 for _ in range(n+1)]

