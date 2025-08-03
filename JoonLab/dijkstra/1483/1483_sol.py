import sys
sys.stdin = open("input.txt")
import heapq

def dijkstra(start_node):
    dists = [float('inf') for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    dists[start_node] = 0
    pq = [(0, start_node)]
    while pq:
        dist, v = heapq.heappop(pq)
        visited[v] = True
        # if v==end_node:
        #     return dists[v]
        for next_info in graph[v]:
            next_weight = next_info[0]
            next_node = next_info[1]
            new_dist = dist+  next_weight
            if dists[next_node] <=new_dist and visited[next_node]:
                continue
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return -1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((w, u))

start, end = map(int, input().split())
_ = int(input()) # 중간 정점의 개수
p = list(map(int, input().split()))

dists, visited = dijkstra(start)
ans = []
for point in p:
    if visited[point]:
        ans.append(True)
    else:
        ans.append(False)
if any(ans):
    if dists[end] != float('inf'):
        print(dists[end])
    else:
        print(-1)
else:
    print(-1)