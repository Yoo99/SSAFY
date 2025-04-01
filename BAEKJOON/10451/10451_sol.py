import sys
sys.stdin = open("10451_input.txt")

def find_node(key):
    global cnt
    visited[key] = True
    print(visited)
    print(cnt)
    for child in graph[key]:
        if child and not visited[child]:
            find_node(child)
        elif child == key:
            cnt+=1
            return cnt
    return cnt

T  = int(input())
for test_case in range(1, T+1):
    n = int(input()) # 숫자의 개수
    graph = {key:[] for key in range(1, n+1)}
    cycle = list(map(int ,input().split()))
    for i in range(0, len(cycle)-1):
        key, val = cycle[i], cycle[i+1]
        graph[key].append(val)
        graph[val].append(key)
    print(graph)
    cnt = 0
    for key in graph.keys():
        visited = [False for _ in range(n+1)]
        print(visited)
        find_node(key)
    print(cnt)
