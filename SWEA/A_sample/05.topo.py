import sys
sys.stdin = open("05.topo_input.txt")
from collections import deque
def find_cycle(start): # 사이클이 존재하는지 확인하는 함수
    global visited
    visited[start] = True
    if rear[start]:
        for child in rear[start]:
            if not visited[child]:
                if find_cycle(child):return True
            elif visited[child] ==1:
                return True
    visited[start] = 2
    return False

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 업무의 개수
    front = {key:[] for key in range(1, N+1)} #선행되어야 할 업무들을 기록해놓음
    rear = {key:[] for key in range(1, N+1)} # 뒤에 오는 노드들을 기록해 놓을 리스트
    work_time = [0 for _ in range(N+1)] # 업무시간을 기록해놓을 리스트
    indepth = [0 for _ in range(N+1)] # 진입 차수 기록할 리스트
    for idx in range(N):
        arr = list(map(int, input().split()))
        if len(arr)==2:
            work_time[idx+1] = arr[0]
            if arr[1]>0:
                front[idx+1].append(arr[1])
                rear[arr[1]].append(idx+1)
            elif arr[1] == 0:
                continue
        else:
            work_time[idx+1] = arr[0]
            for ele in arr[1:]:
                front[idx+1].append(ele)
                rear[ele].append(idx+1)
    # rear graph 완성하기
    # for key in front.keys():
    #     if front[key]:
    #         for parent in front[key]:
    #             rear[parent].append(key)
    print(front)
    print(rear)
    # cycle 존재 여부를 판단하는 코드
    # cycle = False
    # for key in rear.keys():
    #     visited = [False for _ in range(N+1)]
    #     d = find_cycle(key)
    #     if d:
    #         cycle = True
    # if cycle:
    #     print(-1)
    #     continue
    # 진입 차수 확정하는 코드
    queue = deque([])
    for key in front.keys():
        if front[key]==[]:
            queue.append((key,0))
    while queue:
        key,depth = queue.popleft()
        indepth[key] = max(depth, indepth[key])
        if rear[key]:
            for child in rear[key]:
                queue.append((child, depth+1))
    print(indepth[1:]) # 진입 차수를 기록해 놓은 리스트
    depth_max_time = [[] for _ in range(max(indepth)+1)]
    for idx in range(1, len(indepth)):
        depth_max_time[indepth[idx]].append(work_time[idx])
    print(depth_max_time)