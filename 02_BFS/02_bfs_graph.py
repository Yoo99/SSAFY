from collections import deque
def BFS(node):
    # Queue 생성을 해야한다.
    queue = deque([node])
    visited[node] = True
    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        # 내가 가진 모든 자식 노드에 대해서 조사를 진행한다
        for neighbor in graph[vertex]:
            # 해당 정점 방문한 적 있는지 반드시 체크해야 한다
            if not visited[neighbor]:
                queue.append(neighbor)
                # 해당 정점은 조사 대상ㅇ에 등록 되었다.
                visited[neighbor] = True

# 그래프 인접 리스트를 만든다.
graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','E'],
    'D':['B','F'],
    'E':['B','C','F'],
    'F':['D', 'E','G'],
    'G':['F']
}
# node 정보를 key만 뽑아서 list로 만들기
# nodes =  list(graph.keys())
# print(nodes)
# 너비 우선 탐색 -> 방문 표시
visited = {key:False for key in graph.keys()}
# print(visited)
result = []
# BFS('A')
# print(result)
for node in graph:
    if node == 'F':
        BFS(node)
print(*result)
