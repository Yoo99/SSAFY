import sys
sys.stdin = open("input.txt")

from collections import deque
import heapq

N, M = map(int, input().split())
maze = []
for _ in range(N):
    line = list(map(int, input()))
    maze.append(line)
visited = [[1000000000 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
directions = [(-1,0), (0, -1), (1,0), (0,1)]
hq = [(1,0,0)]
while hq:
    dist, x,y = heapq.heappop(hq)
    for dx, dy in directions:
        nx,ny = x+dx , y+ dy
        if 0<=nx<N and 0<=ny<M and maze[nx][ny]==1:
            new_dist = dist + 1
            if visited[nx][ny]> new_dist:
                visited[nx][ny] = new_dist
                heapq.heappush(hq, (new_dist, nx,ny))
print(visited[-1][-1])