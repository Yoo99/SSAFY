import sys
sys.stdin = open("11403_input.txt")
from collections import deque
import heapq

def search(key, graph):
    visited = [False for _ in range(N)]
    hq  = []
    for next in graph[key]:
        hq.append((key, next))
    while hq:
        key, next = hq.pop(0)
        if not visited[next] and ans[key][next]==0:
            ans[key][next] =1
            visited[key] = 1
            for next in
    return ans


N = int(input())
arr = []
graph = {key:[] for key in range(N)}
for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            graph[i].append(j)
            ans[i][j] = 1
visited = [False for _ in range(N)]
print(graph)
for key in graph.keys():
    search(key,graph)
# print(graph)
for idx in range(N):
    print(*ans[idx])