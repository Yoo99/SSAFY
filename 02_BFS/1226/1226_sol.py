import sys
from collections import deque
sys.stdin = open("1226_input.txt","r")

direction = [(-1,0), (1,0), (0, 1), (0,-1)]

def find_flag(idx, idy):
    visited = [[False] * 16 for _ in range(16)]
    queue = deque([(idx,idy)])
    visited[idx][idy] = True
    while queue:
        x,y =queue.popleft()
        for k in range(4):
            dx, dy = direction[k]
            nx = x+ dx ; ny = y + dy
            if 0<=nx<16 and 0<=ny<16 and maze[nx][ny]!=1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                if maze[nx][ny] == 3:
                    return 1
    return 0

for test_case in range(1, 11):
    tc = int(input())
    maze = []
    for i in range(16):
        line = list(map(int, input()))
        maze.append(line)
    # print(maze)
    idx, idy = 0,0
    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                idx = x; idy = y
    print(f"#{tc} {find_flag(idx,idy)}")