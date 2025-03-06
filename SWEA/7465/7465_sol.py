import sys
sys.stdin = open("7465_input.txt")

def find_group(node):
    global semi
    visited[node] = True
    semi.append(node)
    for child in graph[node]:
        if not visited[child]:
            find_group(child)



T = int(input())
for test_case in range(1, T+1):
    N, M=  map(int, input().split()) # N명, 관계의 수_ M개
    graph = {key:[] for key in range(1, N+1)}
    for _ in range(M):
        a,b  = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for _ in range(N+1)]
    final_group = []
    for key in graph.keys():
        if not visited[key]:
            semi = []
            find_group(key)
            if len(semi)>0:
                final_group.append(semi)
    print(f"#{test_case} {len(final_group)}")

