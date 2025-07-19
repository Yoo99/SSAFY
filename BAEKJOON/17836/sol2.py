import sys
sys.stdin = open("17836_input.txt")
from collections import deque

direction = [(-1,0),(0,-1),(1,0),(0,1)] # 상 하 좌 우

def basic(idx,idy,dist):
    global N,M,maze
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque([(idx,idy,0)])
    visited[idx][idy] = True
    while q:
        x,y,w = q.popleft()
        visited[x][y] = True
        for dx, dy in direction:
            nx,ny = dx+x, dy +y
            if 0<=nx<N and 0<=ny<M and maze[nx][ny]!=1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    new_dist = w+1
                    if dist[nx][ny] < new_dist:
                        continue
                    else:
                        dist[nx][ny] = new_dist
                        q.append((nx,ny,new_dist))
            if nx == N-1 and ny==M-1:
                return dist[-1][-1]
    return dist[-1][-1]

def find_sword(idx,idy,dist):
    global N, M, maze, sx,sy
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque([(idx,idy,0)])
    visited[idx][idy] = True
    while q:
        x,y,w = q.popleft()
        visited[x][y] = True
        for dx, dy in direction:
            nx,ny = dx+x, dy+y
            if 0<=nx<N and 0<=ny<M and maze[nx][ny]!=1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    new_dist = w+1
                    if dist[nx][ny]<new_dist:
                        continue
                    else:
                        dist[nx][ny] = new_dist
                        q.append((nx,ny,new_dist))
            if nx==sx and ny ==sy:
                return dist[sx][sy]
    return dist[sx][sy]

N, M, T = map(int,input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dist1 = [[float('inf') for _ in range(M)] for _ in range(N)]
basic = basic(0,0,dist1)
dist2 = [[float('inf') for _ in range(M)] for _ in range(N)]
sx,sy = 0, 0
for idx in range(N):
    for idy in range(M):
        if maze[idx][idy] == 2:
            sx,sy = idx,idy
            break
sword_dist = find_sword(0,0,dist2)
total_sword = sword_dist + (N-1-sx) + (M-1-sy)
result = min(basic, total_sword)
if result <= T:
    print(result)
else:
    print("Fail")