import sys
sys.stdin = open("1753_input.txt")
import heapq

def dijkstra(start_node):
    hq = [(0, start_node)]
    dist[start_node] = 0
    while hq:
        w, v = heapq.heappop(hq)
        # 더 작은 경로로 온 경우가 있다면 패스
        if dist[v] < w:
            continue
        for child in graph[v]:
            new_dist = w+ child[0]
            new_node = child[1]
            if new_dist<dist[new_node]:
                dist[new_node] = new_dist
                heapq.heappush(hq,(new_dist, new_node))
            else:
                continue
    return dist


while True:
    try:
        V,E = map(int, input().split())
        start_node = int(input())
        graph = [[] for _ in range(V + 1)]
        dist = [float('inf') for _ in range(V + 1)]
        for _ in range(E):
            u,v,w = map(int, input().split())
            graph[u].append((w,v)) # 가중치, 도착지점
            # graph[v].append((w,u))
        d = dijkstra(start_node)
        for i in range(1,len(dist)+1):
            if dist[i] == float('inf'):
                print("INF")
            else:
                print(dist[i])

    except:
        break

