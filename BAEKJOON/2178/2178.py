import sys
from collections import deque
sys.stdin = open("2178_input.txt", "r")




# for test_case in range(4):
#     N, M  = map(int, input().split())
#     arr= []
#     visited = [[False] * M for _ in range(N)]
#     for i in range(N):
#         line = list(map(int, input()))
#         arr.append(line)
#     cnt = 0
#     queue =deque([(0,0)])
#     while queue:
#         x,y = queue.popleft()
#         # print(x,y)
#         visited[x][y] = True
#         if arr[x][y] == 1:
#             cnt += 1
#         for dx, dy in direction:
#             nx = x + dx
#             ny = y + dy
#             if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and arr[nx][ny] == 1:
#                 cnt += 1
#                 visited[nx][ny] = True
#                 queue.append((nx,ny))
#                 if nx == N-1 and ny == M-1:
#                     break
#
#     print(cnt)
import sys
input = sys.stdin.readline
from collections import deque
direction = [(-1,0), (0, -1), (0,1), (1,0)]
N,M=  map(int, input().split())
arr = []

for i in range(N):
    line= list(map(int, input().strip()))
    arr.append(line)
cnt = 0
queue = deque([(0,0)])
while queue:
    x,y = queue.popleft()
    if x == N-1 and y == M-1:
        break
    for dx, dy in direction:
        nx = x + dx; ny = y + dy
        if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] +1
            queue.append((nx,ny))

print(arr[-1][-1])