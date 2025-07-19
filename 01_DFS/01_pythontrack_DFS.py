'''
A부터 출발
1) 스택에 넣는다
2) 가장 위 노드를 꺼내면서 방문 처리를 해 주고 스택에 넣어준다
갈 수 있는 노드들을 스택에 넣는다
'''
import sys
sys.stdin = open("graph.txt")
def dfs(node):
    print(node, end = " ")
    visited[node] =  1
    # 내가 갈 수 있는 후보들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지 마라!
        if visited[next_node]:
            continue
        visited[next_node] =1
        dfs(next_node)

N, M = map(int, input().split())
# 1. 그래프를 저장하기
'''
- 비어있는 그래프를 생성한다
- 그래프 정보를 입력받아 넣는다 
'''
# graph = [[0] * N for _ in range(N)]# 인접 행렬 (N * N 의 0배열)
# 인접 리스트(N * N([]))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited  = [0] * (N+1)
dfs(1)
# for row in graph:
#     print(*row)
