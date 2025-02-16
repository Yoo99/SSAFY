import sys
from collections import deque
sys.stdin = open("input2.txt")

N, M = map(int, input().split())
data = [list(map(int,input())) for _ in range(N)]

direction = [(-1,0), (0, 1), (0,-1),(1,0), (-1,1),(1,-1)]

def bfs(idx,idy, acc):
    queue = deque([(idx,idy,acc)])
    while queue:
        x,y,acc = queue.popleft()
        for dx, dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and data[nx][ny]:
                acc+=1
                queue.append((nx,ny, acc))
                data[nx][ny] = 0
    result.append(acc)
result = []
for row in range(N):
    for col in range(M):
        if data[row][col] == 1:
            bfs(row, col, 1)

print(len(result))