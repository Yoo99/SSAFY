# 위상 정렬
# DAG 에서밖에 동작하지 않음. (사이클 X, 방향은 존재)
# 선후 의존성을 고려한 작업 순서를 가져오는 것
# 유일한 해를 보장하지 않는다.
# A -> B -> D
# A => C => D
import sys
sys.stdin = open("1267_input.txt", "r")

def dfs(node):
    visited[node] = True
    for child in graph[node]:
        if child and not visited[child]:
            result.append(child)
            dfs(child)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
print(V,E)
print(arr, len(arr))
keys = [i for i in range(1, V+1)]
graph = {key:[] for key in keys }
for v in range(0, len(arr), 2):
    key, val = arr[v], arr[v+1]
    graph[key].append(val)
print(graph)
visited = [False] * (V+1)
result = []
print(visited)
min_list = []
for key,val in graph.items():
    min_list.append(len(val))
min_idx = min_list.index(min(min_list)) +1
for key in graph.keys():
    visited[key] = True
    for child in graph[key]:
        result.append(child)
        dfs(child)
print(result)