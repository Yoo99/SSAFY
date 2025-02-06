import sys
from collections import deque
sys.stdin = open("1227_input.txt", "r")

direction = [(-1,0), (0,-1), (0,1),(1,0)]

def find_path(idx,idy):
    queue = deque([(idx,idy)])
    while queue:
        x,y= queue.popleft()
        visited[x][y]  = True
        for dx,dy in direction:
            nx = x+dx; ny = y+dy
            if 0<=nx<100 and 0<=ny<100 and arr[nx][ny]!=1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
            if arr[nx][ny] == 3:
                return 1
    return 0


for test_case in range(1, 11):
    N = int(input())
    arr = []
    for i in range(100):
        line= list(map(int, input()))
        arr.append(line)

    idx, idy = 0, 0
    for row in range(100):
        for col in range(100):
            if arr[row][col] ==2:
                idx,idy = row, col
    visited = [[False] *100 for _ in range(100)]
    print(f"#{test_case} {find_path(idx,idy)}")