import sys
from collections import deque
sys.stdin = open("input.txt")

# 1. 전체 공간을 복사해서 각 공간의 좌표마다 시작지점에서 얼마나 이동했나를 표기
# 장점 : 모든 목적지의 최단 거리를 알 수가 있다. (특정 시작 지점 기준으로 한다는 전제 하에)
# 단점 : 메모미를 2배 차지한다.
direction = [(-1,0), (0,-1),(1,0),(0,1)]

def get_road_move_time():
    # q 가 필요함
    # (0, 0) -> (N-1, M-1)
    queue = deque([(0,0)])
    #거리 정보를 지정할 matrix는 어떻게 초기화 해야할까?
    # 방문했는지를 표기하는 역할도 함께 해야 한다.
    distance = [[-1] * M for _ in range(N)]
    distance[0][0] = 0
    while queue:
        x,y = queue.popleft()
        for dx, dy in direction:
            nx = x +dx; ny = y+dy
            # 1. 리스트의 범위를 벗어나지 말아야 한다.
            # 2. 다음 조사 대상이 1 이어야 갈 수 있다.
            # 3. 이전에 방문한 적이 있으면 못간다.
            if 0<=nx<N and 0<=ny<M and data[nx][ny] == 1 and distance[nx][ny]==-1:
                queue.append((nx,ny))
                # 해당 위치까지 이동하는데 걸린 이동 횟수
                distance[nx][ny] = distance[x][y]+1
                if nx ==N-1 and ny == M-1:
                    print(distance)
                    return distance[nx][ny]




N, M = map(int, input().split()) # N, M이 가로인지 세로인지 반드시 확인할 것
data = [list(map(int, input())) for _ in range(N)]
# print(data)
# 최종 결괏값
# 문제에서 도달하지 못했을 때 반환하라고 하는 값을 넣으면 된다.
# 함수 이름을 DFS or BFS로 정의하는 것은 권장하지 않는다.
# 정확한 용도를 작성 해 달라.
# 함수의 역할 : 이동하는데 드는 최소 비용을 구하는 함수
# 이 문제에서는 출발 정점의 x,y 좌표가 고정이다 -> (0, 0)으로 고정이다.
result = get_road_move_time()   # 출발을 시작할 정점 정보
print(result)
