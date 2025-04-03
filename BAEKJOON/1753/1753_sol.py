import sys
sys.stdin = open("1753_input.txt")
import heapq

def dijkstra(start_node):
    dist = [INF for _ in range(V+1)]
    dist[start_node] = 0
    pq = [(0, start_node)]
    while pq:
        dists, node  = heapq.heappop(pq) # 가중치 w와 노드 v
        if dist[node]< dists:
            continue
        for next in graph[node]:
            next_dist = next[0]
            next_node = next[1]
            new_dist = next_dist + dists
            if dist[next_node]<=new_dist:
                continue
            else:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return dist
INF = float('inf')
V,E = map(int,input().split()) # 정점과 간선의 개수
start_node = int(input()) # 시작 노드
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u ,v, w = map(int,input().split())
    graph[u].append((w,v)) # 가중치와 정점을 튜플 형태로 append한다

result = dijkstra(start_node)
for i in range(1, V+1):
    if result[i]== INF:
        print("INF")
    else:
        print(result[i])