import sys
sys.stdin = open("input.txt")

def dijkstra(start_node):
    dists = [float('inf') for _ in range(N+1)]
    pq  = [(0, start_node)]
    dists[start_node] = 0
    while pq:
        dist, v = heapq.heappop(pq)
        for next_info in graph[v]:
            next_weight =  next_info[0]
            next_node = next_info[1]
            new_dist = dist + next_weight
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists



import heapq
N, M = map(int, input().split())
graph  = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))
start_node , end_node = map(int, input().split())

d =dijkstra(start_node)
if d[end_node] == float('inf'):
    print(-1)
else:
    print(d[end_node])