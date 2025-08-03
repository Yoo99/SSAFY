import sys
sys.stdin = open("input.txt")
import heapq

def dijkstra(start_node):
    dists = [float('inf') for _ in range(N+1)]
    dists[start_node] = 0
    pq = [(0, start_node)]
    while pq:
        dist, v = heapq.heappop(pq)
        if dist > dists[v]:
            continue
        for next_info in graph[v]:
            next_weight = next_info[0]
            next_node = next_info[1]
            new_dist = dist+  next_weight
            if dists[next_node] <=new_dist:
                continue
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((w, u))

start, end = map(int, input().split())
_ = int(input()) # 중간 정점의 개수
p = list(map(int, input().split()))

start_dist = dijkstra(start)
end_dist = dijkstra(end)
total = float('inf')
for point in p:
    if start_dist[point] != float('inf') and end_dist[point]!=float('inf'):
        total_dist = start_dist[point] + end_dist[point]
        if total_dist <total:total = total_dist
    else:
        continue
if total>=1000000000000000:
    print(-1)
else:
    print(total)