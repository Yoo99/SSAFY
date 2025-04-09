import sys
sys.stdin = open("24479_input.txt")
from collections import deque

def find(start, graph, N):
    visited = [False for _ in range(N+1)]
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if graph[v]:
            for child in graph[v]:
                if not visited[child]:
                    visited[child] = True
                    queue.append(child)
                else:
                    continue
    return visited


while True:
    try:
        N, M, start = map(int, input().split())
        graph = {key:[] for key in range(1, N+1)}
        for _ in range(M):
            a,b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        d = find(start, graph, N)
        for idx in range(1, len(d)):
            if d[idx]:
                print(idx)
            else:
                print(0)
    except:
        break

