'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v, N):
    visited = [0] * (N+1)
    stack = []

    while True:
        if visited[v] ==0:
            visited[v] = 1
            print(v)
        for w in adj_list[v]:
            if visited[w]==0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break # while을 중단시키는 break
        # v에 인접하고 방문 안 한 w가 있으면

V , E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    v,w = graph[i*2], graph[i*2 +1]
    adj_list[v].append(w)
    adj_list[w].append(v)

dfs(1, V)