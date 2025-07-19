import sys
sys.stdin = open("2814_input.txt")
from collections import deque

def find_path(node,dist):
    visited[node] = True
    queue = deque([])
    queue.extend(graph[node])
    distance[node] = dist
    while queue:
        x= queue.popleft()
        distance[x] = dist
        if graph[x] != []:
            for child in graph[x]:
                if not visited[child] and child in graph[node]:
                    dist +=1
                    print(dist)
                    visited[child] = True
                    find_path(child, dist)
                else:
                    continue
        else:
            break
    return distance

T = int(input()) # test_case의 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    if N ==0 or M ==0 :
        print(f"#{test_case} 1")
        continue
    graph={key:[] for key in range(1, N+1)}
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
        # graph[b].append(a)
    max_dist=  0
    print(graph)
    #     if d>max_dist:
    #         max_dist = d
    #     else:
    #         continue
    # print(f"#{test_case} {max_dist}")
