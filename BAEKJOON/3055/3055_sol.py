import sys
sys.stdin = open("3055_input.txt")
from collections import deque

direction = [(1,0), (0,1), (-1,0), (0,-1)]

def water():
    size=  len(water_queue)
    for _ in range(size):
        x,y = water_queue.popleft()
        for dx, dy in direction:
            nx,ny=  dx+x, dy+y
            if 0<=nx<R and 0<=ny<C and maze[nx][ny]!='X' and maze[nx][ny]=='D':
                maze[nx][ny] = '*'
                water_queue.append((nx,ny))

def find_path(x,y, maze, flag):
    global visited
    queue = deque([(x,y)])
    dist[x][y] = 1
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        water()
        for dx, dy in direction:

            nx, ny = dx+x, dy+y
            if 0<=nx<R and 0<=ny<C and maze[nx][ny] == 'D':
                flag = False
                return flag
            elif 0<=nx<R and 0<=ny<C and not visited[nx][ny] and maze[nx][ny]=='.':
                maze[nx][ny] = 'S'
                dist[nx][ny] = dist[x][y] +1
                visited[nx][ny]=True
                queue.append((nx,ny))
    return flag


R,C = map(int, input().split())
maze = []
for _ in range(R):
    line = list(input())
    maze.append(line)
visited = [[False]*C for _ in range(R)]
idx, idy = 0,0

for row in range(R):
    for col in range(C):
        if maze[row][col] == 'S':
            idx,idy =row, col
flag = True
water_queue = deque([])
dist = [[0]*C for _ in range(R)]
for row in range(R):
    for col in range(C):
        if maze[row][col] == '*':
            water_queue.append((row,col))
find_path(idx,idy, maze, flag)
if flag:
    print("KAKTUS")
else:
    print(max(dist))