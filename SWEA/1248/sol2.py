import sys
sys.stdin = open("1248_input.txt")

def find_depth(node):
    depth[node] +=1
    visited[node] = True
    for child in graph[node]:
        parent[child] = node
        if not visited[child]:
            depth[child] = depth[node]
            find_depth(child)
    return depth

def subtree(node):
    global cnt
    cnt +=1
    visited2[node] = True
    for child in graph[node]:
        if not visited2[child]:
            subtree(child)
    return cnt

T = int(input()) # test case의 개수

for test_case in range(1, T+1):
    V, E, A, B = map(int, input().split())
    graph = {key: [] for key in range(1, V+1)} # 키가 부모
    depth = [0 for _ in range(V+1)]
    parent = [0 for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    line = list(map(int, input().split()))
    for i in range(0,len(line),2):
        graph[line[i]].append(line[i+1])
    find_depth(1)
    ans = 0
    while A!=B:
        if A==B:
            ans = A
            break
        else:
            if depth[A]!=depth[B]:
                if depth[A]>depth[B]:
                    A = parent[A]
                else:
                    B = parent[B]
            if depth[A] == depth[B]:
                A = parent[A]
                B = parent[B]
                if A==B:
                    ans = A
    visited2 = [False for _ in range(V+1)]
    cnt = 0
    subtree(ans)
    print(f"#{test_case} {ans} {cnt}")