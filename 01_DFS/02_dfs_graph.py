# 정점의 개수
V = 7
# 간선의 개수
E = 8
# 간선 정보
'''
그래프의 상황에 따라서 간선 정보가 의미하는 바가 달라질 수 있다. 
1. 무방향 그래프인 경우, 간선의 정보가 한 방향에 대해서 주어지더라도 
1-1. 양쪽 모두로 이어질 수 있음을 의미한다. 
2.   유방향 그래프인 경우, 당연하게도 주어진 간선 정보가 끝. 
2-1. 주어진 정보 그대로 이해하면 된다. 
시작 정점  도착 정점
0         1   # 0번에서 1번 갈 수 있음 
0         2   # 0번에서 2번 갈 수 있음 
1         4
    ...
5         6 
'''
edge_data = [
    [0, 1],
    [0,2],
    # [1,0]  -> 무방향 그래프라서 0 1 이 곧 1 0과 같다.
    [1,3],
    [1,4],
    [3,5],
    [4,5],
    [5,6]
]
visited = [False] * (V+1)

def dfs(now):
    print(now, end = ' ')
    # 조회를 시작했다. now번째를 방문했다.
    visited[now] = True
    for next in range(V):
        # now -> next 이동 가능한지 인접 행렬로 체크
        # next 번째 방문한 적 없는지 체크
        if adj_matrix[now][next] and not visited[next]:
            dfs(next)

adj_matrix = [[0] * V for _ in range(V)]
print(adj_matrix)
for v,e in edge_data:
    adj_matrix[v][e] = 1
    adj_matrix[e][v] = 1
print(adj_matrix)
dfs(0)