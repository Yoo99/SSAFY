import sys
sys.stdin = open("2667_input.txt")
from collections import deque

direction = [(-1,0),(0,-1),(1,0),(0,1)]

N = int(input()) # 한 변의 길이
arr = []
for _ in range(N):
    line = list(map(int,input()))
    arr.append(line)

apt = []
for row in range(N):
    for col in range(N):

        if arr[row][col]==1:
            cnt =0
            queue = deque([(row,col)])
            arr[row][col] = 0

            while queue:
                x,y = queue.popleft()
                cnt +=1
                for dx, dy in direction:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny]==1:
                        queue.append((nx,ny))
                        arr[nx][ny] = 0
            apt.append(cnt)
print(len(apt))
apt.sort()
for i in apt:
    print(i)