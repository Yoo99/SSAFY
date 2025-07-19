import sys
sys.stdin = open("sample_input.txt")
import heapq


def dijkstra(node):
    hq = [(0,node)]
    dist[node] = 0
    while hq:
        w,y = heapq.heappop(hq)
        if graph[y]:
            for child in graph[y]:
                new_dist = child[0] + w
                new_node = child[1]
                if new_dist>dist[new_node]:
                    continue
                dist[new_node] = new_dist
                heapq.heappush(hq, (new_dist, new_node))
    return dist



N, M , C = map(int, input().split())
graph={key : [] for key in range(1, N+1)}
dist = [float('inf') for _ in range(N+1)]
hq = heapq.heapify([])
for _ in range(M):
    x,y,z = map(int,input().split()) # x: 출발지, y: 도착지, w: 가중치
    graph[x].append((z,y))
d = dijkstra(C)
max_num = 0
for idx in d:
    if idx == float('inf'):
        continue
    elif idx>max_num:
        max_num = idx
print(max_num)

