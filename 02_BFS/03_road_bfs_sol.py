import sys
from collections import deque
sys.stdin = open("input.txt")

direction = [(-1,0), (0,1), (0,-1),(1,0)]

N,M=  map(int, input().split())
arr = []
for row in range(N):
    line = list(map(int, input()))
    arr.append(line)
visited = [[False] *M for _ in range(N)]
cnt = 0
queue = deque([0,0,])
def bfs(idx, idy):
    queue = deque([(idx,idy, arr[idx][idy])])
    while queue:
        idx, idy, M = queue.popleft()
        # print(idx,idy)
        for dx, dy in direction:
            nx = idx + dx; ny = idy + dy
            while 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] ==1:
                arr[nx][ny] +=M
                visited[nx][ny] = True
                queue.append((nx,ny, arr[nx][ny]))
            if nx == N-1 and ny == M-1:
                return


# for row in  range(N):
#     for col in range(M):
#         visited[row][col] = True
#         for dx, dy in direction:
#             nx = row + dx; ny = col + dy
#             while 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] ==1:
#                 print(nx,ny)
#                 visited[nx][ny] =True
#                 cnt += 1
#                 nx = nx +dx;  ny = ny+dy
#                 if nx == N-1 and ny == M-1:
#                     break
bfs(0,0)
