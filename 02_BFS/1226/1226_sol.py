import sys
from collections import deque
sys.stdin = open("1226_input.txt","r")

direction = [(-1,0),(0,1),(1,0),(0,-1)]

def find_path(idx, idy):
    visited = [[False] * 16 for _ in range(16)]
    queue = deque([(idx,idy)])
    visited[idx][idy] = True
    while queue:
        x,y = queue.popleft()
        for dx, dy in direction:
            nx,ny = x+dx, y+dy
            if 0<=nx<16 and 0<=ny<16 and not visited[nx][ny] and arr[nx][ny]!=1:
                visited[nx][ny] = True
                queue.append((nx,ny))
                if arr[nx][ny] ==3:
                    return 1
    return 0



for test_case in range(1, 11):
    N=  int(input())
    arr = []
    for i in range(16):
        line=  list(map(int,input()))
        arr.append(line)


    for row in range(16):
        for col in range(16):
            if arr[row][col] ==2:
                result = find_path(row, col)
                print(f"#{test_case} {result}")


