def bfs(s,V): # 시작 정점
    # visited 생성
    # 큐  생성
    # 시작점 인큐
    # 시작점 인큐 표시
    # 큐가 비워질 때 까지 반복
    visited = [0] * (V+1)
    q = []
    q.append(s)
    visited[s] = 1
    while q: # 큐가 비워질 때까지 반복, front != rear
        t = q.pop(0)      # 디큐해서 t에 저장
        print(t)# t 정점에 대한 처리
        for w in adj_1[t]: # t에 인접한 정점 w 중, 인큐되지 않은 정점이 있으면
            if visited[w] ==0:
                q.append(w)
                visited[w] = visited[t] +1

        # 인큐하고 인큐 표시한다

V, E = map(int, input().split())
arr = list(map(int ,input().split()))

adj_l = [[] for _ in range(V+1)]
for i in range(0, E*2, 2):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1) # 무방향 그래프인 경우

bfs(1,7)