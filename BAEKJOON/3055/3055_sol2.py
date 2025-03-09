import sys
sys.stdin = open("3055_input.txt")
from collections import deque

direction = [(-1,0),(0,-1),(1,0),(0,1)]

def find_path(x,y,water_queue):
    queue = deque([(x,y)])
    while queue:
        size = len(water_queue)
        for _ in range(size):
            wx,wy = water_queue.popleft()
            for dx, dy in direction:
                wnx, wny= dx+wx, dy+wy
                if 0<=wnx<R and 0<=wny<C and maze[wnx][wny]=='.' and not visited[wnx][wny]:
                    maze[wnx][wny] = '*'
                    visited[wnx][wny] = True
                    water_queue.append((wnx,wny))

        size_queue = len(queue)
        for _ in range(size_queue):
            x,y = queue.popleft()
            for dx,dy in direction:
                nx,ny = x+dx, y+dy
                if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and maze[nx][ny] == 'D':
                    dist[nx][ny] = dist[x][y] + 1
                    return dist[nx][ny]
                # 물일 경우에
                elif 0<=nx<R and 0<=ny<C  and maze[x][y] =='S' and maze[nx][ny] !='X' and maze[nx][ny]!='*' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maze[nx][ny] = 'S'
                    dist[nx][ny] = dist[x][y] +1
                    queue.append((nx,ny))

    return "KAKTUS"



R, C = map(int,input().split())
maze = []
for _ in range(R):
    line=  list(input())
    maze.append(line)
# 방문했던 곳을 재방문하지 않기 위해
visited = [[False] * C for _ in range(R)]
# 최단 경로를 계산하기 위한 2차원 배열
dist = [[0]*C for _ in range(R)]
water_queue = deque([])
# 고슴도치 S의 좌표 확인 (idx, idy) / 비버의 굴 위치 확인 (DX,DY)
for row in range(R):
    for col in range(C):
        if maze[row][col] == 'S':
            idx,idy = row, col
        elif maze[row][col] == 'D':
            DX,DY = row, col
        elif maze[row][col] == '*':
            water_queue.append((row,col))
visited[idx][idy] = True
print(find_path(idx,idy, water_queue))
