import sys
from collections import deque
sys.stdin = open("1227_input.txt", "r")

direction = [(-1,0), (0,-1), (0,1),(1,0)]

def find_flag(idx,idy):
    visited = [[False]*100 for _ in range(100)]
    queue = deque([(idx,idy)])
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if 0<=nx<100 and 0<=ny<100 and not visited[nx][ny] and maze[nx][ny]!=1:
                if maze[nx][ny]==3:
                    return 1
                queue.append((nx,ny))
    return 0

for test_case in range(1,11):
    _ = int(input())
    maze = []
    for row in range(100):
        line = list(map(int, input()))
        maze.append(line)
    for row in range(100):
        for col in range(100):
            if maze[row][col] ==2:
                result = find_flag(row, col)
    print(f"#{test_case} {result}")