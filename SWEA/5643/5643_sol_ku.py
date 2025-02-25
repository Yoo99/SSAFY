import sys
sys.stdin = open('5643_input.txt')  # 필요시 사용


# node: 조사 시작 노드
# graph: forward or backward
# visited: 각 조사에 대한 방문 표시
def search(node, graph, visited):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            search(next, graph, visited)

T = int(input())
for tc in range(1, T+1):
    # N: 학생 수, M: 간선 수
    N = int(input())
    M = int(input())

    # 그래프 초기화
    # 0번 노드 없음.
    forward_graph = [[] for _ in range(N+1)]   # 정방향: a->b (a<b)
    backward_graph = [[] for _ in range(N+1)]  # 역방향: b->a (b>a)

    # 간선 정보 입력
    for _ in range(M):
        a, b = map(int, input().split())
        forward_graph[a].append(b)
        backward_graph[b].append(a)
    # print(forward_graph, backward_graph)
    print("forward_graph", forward_graph)
    print("backward_graph", backward_graph)
    result = 0
    # 각 학생 i에 대해, i보다 큰 학생 수/작은 학생 수 확인
    for i in range(1, N+1):
        # 1. i보다 큰 학생 수 구하기 (정방향)
        visited = [False] * (N+1)
        search(i, forward_graph, visited)
        bigger_count = sum(visited) - 1  # 자기 자신 제외

        # 2. i보다 작은 학생 수 구하기 (역방향)
        visited = [False] * (N+1)
        search(i, backward_graph, visited)
        smaller_count = sum(visited) - 1  # 자기 자신 제외

        # 3. 순위가 확실한지 확인 (마찬가지로 자기자신 제외한 모든 노드)
        if bigger_count + smaller_count == N - 1:
            result += 1

    print(f'#{tc} {result}')
