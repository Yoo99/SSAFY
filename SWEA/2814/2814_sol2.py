import sys
sys.stdin = open("2814_input.txt")
import heapq

def find_path(node):
    visited = [False for _ in range(N+1)]
    dist = [0 for _ in range(N+1)]
    visited[node] = True
    hq = [(1, node)]
    while hq:
        w,y = heapq.heappop(hq)
        dist[y] = w
        if graph[y]:
            for child in graph[y]:
                if not visited[child]:
                    dist[child] = w+1
                    visited[child] = True
                    heapq.heappush(hq, (dist[child], child))
                else:continue
    return dist

T= int(input()) # tet_case의 개수
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    graph = {key:[] for key in range(1, N+1)}
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    max_dist = 0
    for key in graph.keys():
        d=  find_path(key)
        if max(d) > max_dist:
            max_dist = max(d)
        else:
            continue
    print(f"#{test_case} {max_dist}")