import sys
sys.stdin = open("1916_input.txt")
import heapq

def dijkstra(start_node):
    INF = float('inf')
    dist = [INF] * (N+1)
    hq = [(0, start_node)]
    while hq:
        w, next = heapq.heappop(hq)
        if dist[next]<w:
            continue
        for child in graph[next]:
            next_dist = child[0]
            next_node = child[1]
            temp_dist = w + next_dist
            if dist[next_node] > temp_dist:
                dist[next_node] = temp_dist
                heapq.heappush(hq,(temp_dist, next_node))
            else:continue
    return dist

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v, w = map(int, input().split()) # 출발점, 도착점, 비용
    graph[u].append((w,v)) # 비용, 도착점으로 저장
start_node, end_node = map(int,input().split())
d= dijkstra(start_node)
print(d[end_node])