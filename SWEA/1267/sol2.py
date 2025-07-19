import sys
sys.stdin = open("1267_input.txt")
from collections import deque

# 위상정렬 함수
def topology_sort():
    global index_list
    result = []
    queue = deque([])
    for i in range(1, len(index_list)):
        if index_list[i] ==0:
            queue.append(i) # 진입차수가 0인 애들을 queue에다가 삽입
    while queue:
        a = queue.popleft() #queue에 들어있던 애를 뺀다
        result.append(a) # 결과 리스트에다가 추가
        for ele in graph[a]: # 연관된 노드들의 진입차수를 1씩 줄여준다
            index_list[ele] -=1
            if index_list[ele] ==0:
                queue.append(ele)
    return result


for test_case in range(1, 11):
    V, M = map(int, input().split()) # v: 정점의 개수
    graph = {key:[] for key in range(1, V+1)} # 그래프 정보 기록
    arr = list(map(int, input().split())) # 배열을 받은 것
    index_list = [0 for _ in range(V+1)]
    for i in range(0, len(arr), 2):
        a,b = arr[i], arr[i+1]
        graph[a].append(b)
        index_list[b]+=1
    d = topology_sort()
    print(f"#{test_case}", end = ' ')
    print(*d)

