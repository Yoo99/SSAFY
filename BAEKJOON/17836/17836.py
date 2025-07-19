import sys
sys.stdin = open("17836_input.txt")
from collections import deque

direction = [(-1, 0), (0, -1), (1,0), (0,1)] # 상하좌우 방향 그래프

def dijkstra(idx, idy, dist): # 출발점 x,y 좌표 넣기
    global maze, N,M
    hq = deque([(maze[idx][idy], idx,idy)]) # 가중치와 x좌표, y좌표
    while hq:
        w, x,y = hq.popleft()
        for dx, dy in direction:
            nx,ny = x+dx, y + dy
            if 0<=nx<M and 0<=ny<N and maze[nx][ny]!=1:
                new_dist = w + 1
                if dist[nx][ny] < new_dist:
                    continue
                else:
                    dist[nx][ny] = new_dist
                    hq.append((new_dist, nx,ny))
            if nx==M-1 and ny ==N-1:
                return dist[-1][-1]
    return dist[-1][-1]

def find_sword(idx,idy, dist):
    global maze, N, M, sx,sy
    hq = deque([(maze[idx][idy], idx,idy)])
    while hq:
        w,x,y = hq.popleft()
        for dx, dy in direction:
            nx,ny = x+dx, y+dy
            if 0<=nx<M and 0<=ny<N and maze[nx][ny]!=1:
                new_dist = w+1
                if dist[nx][ny] < new_dist:
                    continue
                else:
                    dist[nx][ny] = new_dist
                    hq.append((new_dist, nx,ny))
            if nx==sx and ny==sy:
                return dist[sx][sy]
    return dist[sx][sy]

N, M, T = map(int, input().split()) # 행의 개수, 열의 개수, 제한시간
# 두가지 케이스를 모두 구해서 그 중에 제일 시간이 적게 걸리는 애를 구하기
maze = [list(map(int, input().split())) for _ in range(N)] # 미로 형태를 받기
# 그람을 구하지않고 그냥 정석대로 가는 경우
dist1 = [[float('inf') for _ in range(M)] for _ in range(N)]
dist1[0][0] = maze[0][0] # 출발점 초기화
without_sword = dijkstra(0,0,dist1)
if without_sword == float('inf'):
    print("Fail")
# 그람을 무조건 구하고 공주를 구하러 가는 경우
# 그람이 있는 위치 좌표를 구하기
sx, sy = 0,0
for idx in range(N):
    for idy in range(M):
        if maze[idx][idy] ==2:
            sx,sy = idx,idy
            break
dist2 = [[float('inf') for _ in range(M)] for _ in range(N)]
dist2[0][0] = maze[0][0]
sword_dist = find_sword(0,0,dist2) + (M-1-sx) + (N-1-sy)
result = min(without_sword, sword_dist)
if result <=T:
    print(result)
else:
    print("Fail")

