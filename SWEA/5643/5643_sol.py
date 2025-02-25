import sys
sys.stdin = open("5643_input.txt")
<<<<<<< HEAD

def search(node, graph, visited):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            search(next, graph, visited)


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 학생들의 수
    M = int(input()) # 비교 횟수
    forward_graph = [[] for _ in range(N+1)]
    backward_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        forward_graph[a].append(b)
        backward_graph[b].append(a)
    # print(forward_graph)
    # print(backward_graph)

    result = 0
    # 각 학생 i에 대해서 i보다 큰 학생 수/작은 학생 수 확인하기
    for i in range(1, N+1):
        visited = [False] * (N+1)
        search(i, forward_graph, visited)
        bigger_count = sum(visited) -1 # 자기 자신 제외

        # 학생 i보다 작은 학생 수 구하기 (역방향)
        visited = [False] *(N+1)
        search(i, backward_graph, visited)
        smaller_count = sum(visited)-1
        if bigger_count + smaller_count == N-1:
            result +=1
    print(f"#{test_case} {result}")
=======
from collections import deque

T = int(input())
N = int(input()) # 학생들의 숫자
M = int(input()) # 학생들의 키를 비교한 결과
keys = [i for i in range(1, N+1)]
student = {key:[] for key in keys}

for j in range(M):
    a,b = map(int, input().split())
    student[a].append(b)
print(student)
height = deque()

for key,value in student:
    if value != []:
        if key not in height:
            height.appendleft(key)
            height.append()
>>>>>>> 0dd699f0e70f3a1a658e9fb2f51913ef87901dce


