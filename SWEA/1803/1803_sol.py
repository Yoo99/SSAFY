import sys
sys.stdin = open("1803_input.txt")
import heapq

def find_path(start,end):
    hq = [(0, start)]
    visited[start] = True
    dist[start] = 0
    while hq:
        w,x = heapq.heappop(hq)
        visited[x] = True
        dist[x] = w
        if x == end:
            return dist
        if graph[x]:
            for child in graph[x]:
                if not visited[child[1]]:
                    new_dist = w + child[0]
                    new_node = child[1]
                    if new_dist>dist[new_node]:
                        continue
                    dist[new_node] = new_dist
                    heapq.heappush(hq, (new_dist, new_node))
                else:
                    continue
    return dist


T = int(input()) # 테스트 케이스의 개수
for test_case in range(1, T+1):
    N, M , s, e= map(int, input().split())
    graph = {key:[] for key in range(1, N+1)}
    for _ in range(M):
        a,b,w =map(int, input().split())
        graph[a].append((w,b))
        graph[b].append((w,a))
    dist = [float('inf') for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    print(f"#{test_case} {find_path(s,e)[e]}")