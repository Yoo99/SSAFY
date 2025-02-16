import sys
sys.stdin = open("input.txt")
from collections import deque

# 방문할 정점 + 지금까지 이동하는데 든 비용을 모두 queue에 삽입한다.
# 4방향에 대한 조사 방법도 다른 방법도 해보자.
# 상하좌우 idx

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def get_road_move_time():
    # x,y, acc
    # 누적값을 넣어도 ... visited는 똑같이 필요하다
    queue = deque([(0,0,0)])
    visited = [[False] * M for _ in range(N)]
    while queue:
        x,y,dist = queue.popleft()
        for k in range(4):
            nx,ny = x + dx[k] , y+dy[k]
            next_dist = dist +1
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and data[nx][ny]:
                queue.append((nx,ny,next_dist))
                if nx ==N-1 and ny == M-1:
                    return next_dist
    return -1

N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

result = get_road_move_time()
print(result)