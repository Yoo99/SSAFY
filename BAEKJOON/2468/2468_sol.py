import sys
sys.stdin = open("2468_input.txt")
from collections import deque

direction = [(-1,0),(0,-1),(1,0),(0,1)]

N= int(input())
arr = []
height = []
for _ in range(N):
    line = list(map(int, input().split()))
    for ele in line:
        if ele not in height:
            height.append(ele)
    arr.append(line)
max_area = 0
for h in range(0, max(height)):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col]> h and not visited[row][col]:
                queue = deque([(row,col)])
                visited[row][col] = True
                while queue:
                    x,y = queue.popleft()
                    for dx, dy in direction:
                        nx,ny = x+dx, y + dy
                        if 0<=nx<N and 0<=ny<N and arr[nx][ny]>h and not visited[nx][ny]:
                            queue.append((nx,ny))
                            visited[nx][ny] = True
                cnt +=1
    if cnt>max_area:
        max_area = cnt
print(max_area)