# 정점의 개수
V = 7
# 간선의 개수
E = 8
# 간선 정보
'''
그래프의 상황에 따라서 간선 정보가 의미하는 바가 달라질 수 있다. 
1. 무방향 그래프인 경우, 간선의 정보가 한 방향에 대해서 주어지더라도 
1-1. 양쪽 모두로 이어질 수 있음을 의미한다. 
2. 유방향 그래프인 경우, 당연하게도 주어진 간선 정보가 끝. 
2-1. 주어진 정보 그대로 이해하면 된다. 
시작 정점 , 도착 정점 
0 1
0 2 
1 4
```
5 6 
'''
edge_data = [
    [0,1], [0,2],[1,3],[1,4],
    # [1, 0] -> 무방향 그래프라서 0 1이 곧 1 0과 같다.
    [2,4],[3,5],[4,5],[5,6]

]

def dfs(now):
    print(now, end  = ' ')
    # 조회를 시작했다. now번째를 방문했다.
    visited[now] = True
    for next in range(V): # 내가 가진 모든 정점에 대해서
        # now -> next 이동 가능한지 인접 행렬로 체크
        # next 번째 방문한 적이 없는지 체크

        if adj_matrix[now][next] and not visited[next]:
            dfs(next)
'''         
adj = {0:[1,2], 1:[0,3,4], 2:[0,4], 3:[5,1], 4:[1,2,5], 5:[3,4,6], 
'''
# adj = [[1,2],[0,1,2],[0,4]...]
# 인접 행렬 방식으로 나타내기
# 모든 노드의 개수만큼 만든다.  V * V만큼 만든다.
adj_matrix  = [[0] * V for _ in range(V)]
# 간선의 개수 만큼 간선 정보를 순회해서 인접 행렬에 값을 적자
for idx in range(E):
    S,E = edge_data[idx]
    adj_matrix[S][E] = 1 # 인접 정보 재할당
    # 무방향 그래프 이므로 반대도 똑깥이 해준다.
    adj_matrix[E][S] = 1
# for row in adj_matrix:
#     print(row)
# 현재 해당 노드를 방문한 전적이 있는지 체크하기 위한 리스트
visited = [False] * V # 모든 정점에 대해서 기록하기 위해 만들기 때문에
# 0    1    2     3    4   5    6
# [False, False, False, False, False, False]
#내가 방문 가능한 대상인지만 골라먹기? XXXXX
# 모든 정점에 대해서 방문 가능한 여부는 ? adj_matrix에 표기해뒀다.
for idx in range(V):
    # 해당 노드를 한 번이라도 방문한 적이 있다면
    if visited[idx]:
        continue # 아무것도 하지 않고, 다음 노드로 넘긴다
    # 시작정점 : idx -> 0으로 조회를 시작
    dfs(0)