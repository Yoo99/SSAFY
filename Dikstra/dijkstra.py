import sys
sys.stdin = open("graph.txt")

def dijkstra(start_node):
    pq = [(0,start_node)] # 누적 거리, 노드 번호
    dist = [INF] * V    # 각 정점까지의 최단 거리를 저장할 리스트
    dist[start_node] = 0 # 시작 노드 최단 거리는 0

    while pq:
        dists,node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        # 예제 그림: c로 가는 경로가 3 or 4
        if dist[node] < dists:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0] # 다음 노드로 가기 위한 가중치
            next_node = next_info[1] # 다음 노드 번호

            # 다음 노드로 가기 위한 누적 거리
            new_dist = dists + next_dist
            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if new_dist >= dist[next_node]:
                continue
            else:
                dist[next_node] = new_dist # next_node까지 도착하는 데 드는 비용은 new_dist입니다.
                heapq.heappush(pq, (new_dist, next_node))
    return dist
import heapq
INF = float('inf')

V, E = map(int, input().split())
start_node = 0 # 출발 노드
graph = [[] for _ in range(V)] # 인접 리스트로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v)) # 단방향 그래프
print(graph)
results = dijkstra(0)
print(results)