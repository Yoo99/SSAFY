import sys
sys.stdin = open("10159_input.txt")
input=  sys.stdin.readline

def search(node,graph,visited):
    visited[node] =  True
    for next in graph[node]:
        if not visited[next]:
            search(next, graph, visited)

N  = int(input().strip()) # 물건의 개수
M = int(input().strip()) # 물건 쌍의 개수
forward_graph = [[] for _ in range(N+1)]
backward_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    forward_graph[a].append(b)
    backward_graph[b].append(a)
ans = [0 for _ in range(N+1)]
for i in range(1, N+1):
    result = 0
    visited = [False for _ in range(N+1)]
    search(i, forward_graph, visited)
    bigger_count = sum(visited)

    visited = [False for _ in range(N+1)]
    search(i,backward_graph, visited)
    smaller_count = sum(visited)
    result = bigger_count+smaller_count-1
    ans[i] = N - result
for j in range(1, len(ans)):
    print(ans[j])
