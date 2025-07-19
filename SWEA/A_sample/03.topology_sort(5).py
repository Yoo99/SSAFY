import sys
sys.stdin = open("03.topology_sort_input.txt")
from collections import deque

T = int(input()) # test case의 개수
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V : 과목 수 , E: 선행 과목이 있는 과목쌍
    graph = {key:[] for key in range(1, V+1)}
    depth = [0 for _ in range(V+1)]
    front = [[] for _ in range(V+1)]
    rear = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        a,b = arr[i], arr[i+1]
        graph[a].append(b)
        front[b].append(a)
        rear[a].append(b)
        depth[b] +=1
    # print(front)
    # print(depth)
    result = [0 for _ in range(V+1)]
    queue = deque([])
    for idx in range(1, len(depth)):
        if depth[idx] == 0:
            queue.append((idx, 1))

    while queue:
        d, w = queue.popleft()
        result[d] = w
        for ele in rear[d]:
            depth[ele]-=1
            if depth[ele] == 0:
                max_v = 0
                for dx in front[ele]:
                    max_v = max(max_v, result[dx])
                queue.append((ele, max_v+1))
    print(f"#{test_case} {max(result)}")

