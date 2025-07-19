import sys
sys.stdin = open("2458_input.txt")

def search_node(start,graph, visited):
    visited[start] = True
    if graph[start]:
        for child in graph[start]:
            if not visited[child]:
                search_node(child, graph, visited)
    return visited
while True:
    try:
        N, M  = map(int ,input().split()) # 학생 수, 비교 횟수
        taller = [[] for _ in range(N+1)]
        smaller  = [[] for _ in range(N+1)]
        height = [0 for _ in range(N+1)] # 결과를 담을 리스트
        for _ in range(M):
            a,b = map(int, input().split())
            taller[a].append(b)
            smaller[b].append(a)
        # 각 노드별로 해당 노드보다 키가 더 큰 학생 수를 카운팅, 키가 더 작은 학생 수 카운팅
        person = 0
        for start in range(1, N+1):
            visited1 = [False for _ in range(N+1)]
            visited2 = [False for _ in range(N+1)]
            smaller_count = sum(search_node(start, smaller, visited1))
            bigger_count =  sum(search_node(start, taller, visited2))
            total = smaller_count + bigger_count -1
            if total == N:
                person +=1
        print(person)
    except:
        break