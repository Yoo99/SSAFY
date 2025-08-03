import sys
sys.stdin = open("graph.txt")


def dijkstra(start_node):
    pq = [(0, start_node)] # 누적 거리와 노드 번호
    dists = [INF] * V # 각 정점까지의 최단 거리를 저장할 리스트
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass 한다
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_weight = next_info[0] # 다음 노드로 가기 위한 가중치
            next_node = next_info[1]
            new_dist = dist + next_weight
            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if new_dist >= dists[next_node]:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

import heapq
INF = int(21e8) # 21억 무한대를 의미한다고 가정

V, E  = map(int, input().split()) # 노드 수 와 간선 수
start_node = 0  # 문제에 따라 다름

graph = [[] for _ in range(V)] # 인접 리스트로 구현

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w, v)) # 단방향 그래프이다

result_dist = dijkstra(0)
print(result_dist)