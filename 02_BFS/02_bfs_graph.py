from collections import deque

# 그래프 인접 리스트
def BFS(node):
    # Q 생성
    queue = deque([node])
    visited[node] = True
    while queue:
        vertex = queue.popleft()
        result.append(vertex)  # global에 있는 result의 값을 변환하는 것이 아닌 result가 참조하는
        # list를 변환하는 것이기 때문에 가능한 것

        # 내가 가진 모든 자식 노드에 대해서 조사
        for neighbor in graph[vertex]:
            # 해당 정점을 방문한 적이 있는지 반드시 체크
            if not visited[neighbor]:
                queue.append(neighbor)
                # 해당 정점은 조사 대상에 등록이 되었다.
                visited[neighbor] = True
    return result


graph = {
    'A': ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','E'],
    'D' : ['B','F'],
    'E' : ['B','C','F'],
    'F' : ['D','E','G'],
    'G' : ['F']
}
# node 정보를 key만 뽑아서 리스트로 만들기
nodes = list(graph.keys())
# print(nodes)
# 너비 우선 탐색 -> 방문 표시
visited  = {key:False for key  in graph}
result = []
# BFS('A')
# print(*result)
# 만약에 다른 node에서 시작하고 싶을 때
for node in graph:
    if node == 'F':
        BFS(node)
print(*result)