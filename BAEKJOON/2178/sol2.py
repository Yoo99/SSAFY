import sys
sys.stdin = open("2178_input.txt")
from collections import deque

direction = [(-1,0),(0,-1),(1,0),(0,1)]

N, M = map(int, input().split())
maze = []
for _ in range(N):
    line=  list(map(int, input()))
    maze.append(line)

visited = [[False] * M for _ in range(N)]
for row in range(N):
    for col in range(M):
        visited[row][col] = True
dist = [[100000000] *M for _ in range(N)]
visited =[[False]*M for _ in range(N)]
dist[0][0] = 1

queue = deque([(0,0)])

while queue:
    dx, dy = queue.popleft()
    visited[dx][dy] = True
    for cx, cy in direction:
        nx, ny = dx + cx, dy+cy
        if 0<=nx<N and 0<=ny<M and maze[nx][ny]==1 and not visited[nx][ny] and dist[dx][dy] + 1< dist[nx][ny]:
            visited[nx][ny] = True
            dist[nx][ny] = dist[dx][dy] + maze[nx][ny]
            queue.append((nx,ny))
        if nx ==N-1 and ny==M-1:
            break

print(dist[-1][-1])