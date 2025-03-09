import sys
sys.stdin = open("1260_input.txt")
from collections import deque

def dfs_search(v,graph):
    global visited
    global arr
    visited[v]  = True
    arr.append(v)
    for child in sorted(graph[v]):
        if not visited[child]:
            dfs_search(child, graph)

    return arr

def bfs_search(v, graph):
    global visited
    visited[v]  = True
    queue = deque([v])
    result = []
    while queue:
        key = queue.popleft()
        result.append(key)
        for child in sorted(graph[key]):
            if not visited[child]:
                visited[child] = True
                queue.append((child))

    return result

N, M, V = map(int, input().split())
keys = [i for i in range(1, N+1)]
graph  = {key:[] for key in keys}
for _ in range(M):
    A,B = map(int ,input().split())
    graph[A].append(B)
    graph[B].append(A)

# DFS 수행을 위한 작업
visited = [False for _ in range(N+1)]
arr = []
for ele in dfs_search(V,graph):
    print(ele, end=  ' ')
print()
visited = [False for _ in range(N+1)]
for ele in bfs_search(V, graph):
    print(ele, end = ' ')
print()