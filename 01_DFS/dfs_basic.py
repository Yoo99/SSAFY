def dfs(v,N): # v 출발, N 마지막 정점
    visited = [0] *(N+1)   # 방문 표시
    stack = []             # 스택

    while True:
        if visited[v] == 0: # 첫 방문이면
            visited[v] = 1
            print(v)
        for w in adj_list[v]: # v에 인접하고 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v) # 현재 정점을 push
                v = w           # w로 이동
                break           # for문에 대한 중단
            else:
                if stack:
                    v = stack.pop()
                else:
                    break # while 중단

V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    v, w = graph[i*2] , graph[i*2+1]

    adj_list[v].append(w)
    adj_list[w].append(v)

dfs(1, V)
