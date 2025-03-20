import sys
sys.stdin = open("1012_input2.txt")
from collections import deque

direction = [(-1,0,), (0,1),(1,0),(0,-1)]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    for _ in range(K):
        x,y = map(int, input().split())
        arr[x][y] = 1
    spot = []
    visited = [[False] * N for _ in range(M)]
    for row in range(M):
        for col in range(N):
            if arr[row][col] ==1 and not visited[row][col]:
                cnt = 0
                arr[row][col] = 0
                queue = deque([(row, col)])
                while queue:
                    cx,cy = queue.popleft()
                    visited[cx][cy] = True
                    cnt +=1
                    for dx, dy in direction:
                        nx,ny= cx + dx, cy +dy
                        if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 1 and not visited[nx][ny]:
                            queue.append((nx,ny))
                            arr[nx][ny] = 0
                spot.append(cnt)
    print(len(spot))

