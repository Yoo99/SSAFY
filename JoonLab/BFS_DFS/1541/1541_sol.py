import sys
sys.stdin =open("input.txt")

from collections import deque


maze = []
direction = [(-1,0), (0,-1), (1,0),(0,1)]
for _ in range(5):
    line = list(map(int, input().split()))
    maze.append(line)
r,c = map(int, input().split())
visited = [[False] *5 for _ in range(5)]
dist = [[10000] * 5 for _ in range(5)]
def find_path(maze, r,c,visited, dist):
    q = deque()
    visited[r][c] = True # 시작점
    dist[r][c] = 0
    q.append((r, c, dist[r][c]))
    while q:
        x,y,distance = q.popleft()
        if maze[x][y]==1:
            return dist[x][y]
        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and maze[nx][ny]!=-1:
                visited[nx][ny] = True
                dist[nx][ny] = distance+1
                q.append((nx,ny, dist[nx][ny]))


        for dx, dy in direction:
            cx,cy = x,y
            while True:
                nx,ny = cx+dx, cy + dy
                # cx, cy = nx, ny
                if 0<=nx<5 and 0<=ny<5 and maze[nx][ny]!=-1 and maze[nx][ny]!=7:
                    cx,cy = nx,ny

                else:
                    break
            if not visited[cx][cy] and maze[cx][cy] != -1:
                visited[cx][cy] = True
                dist[cx][cy] = dist[x][y] +1
                q.append((cx,cy, dist[cx][cy]))


    return -1


print(find_path(maze, r,c,visited, dist))