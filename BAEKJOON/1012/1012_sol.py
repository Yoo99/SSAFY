import sys
sys.stdin = open("1012_input.txt")
from collections import deque

direction = [(-1,0,), (0,1),(1,0),(0,-1)]

def bfs(row, col, cnt):
    for dx,dy in direction:
        nx,ny = row + dx, dy + col
        if 0<=nx<M and 0<=ny<N and arr[nx][ny] ==1:
            cnt +=1
            queue.append((nx,ny, cnt))
            arr[nx][ny] = 0
        else:
            spot.append(cnt)





T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    for _ in range(K):
        x,y = map(int, input().split())
        arr[x][y] = 1
    spot = []
    for row in arr:
        print(row)
    visited = [[False]*N for _ in range(M)]
    for row in range(M):
        for col in range(N):
            if arr[row][col] ==1:
                cnt = 0
                queue = deque([(row,col,cnt)])
                while queue:
                    row,col,cnt = queue.popleft()
                    arr[row][col] = 0
                    cnt +=1
                    for dx, dy in direction:
                        nx, ny = row + dx, dy + col
                        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny]:
                            cnt += 1
                            queue.append((nx, ny, cnt))
                            arr[nx][ny] = 0
                spot.append(cnt)

    print(spot)