import sys
from collections import deque
sys.stdin = open("1249_input.txt","r")

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def find_path(arr):
    queue = deque([(0,0)])
    dist[0][0] = arr[0][0]
    while queue:
        x,y = queue.popleft()
        acc = dist[x][y]
        for dx, dy in direction:
            nx,ny = dx+x, dy+y
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] + acc<dist[nx][ny]:
                    dist[nx][ny] = arr[nx][ny] + acc
                    queue.append((nx,ny))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        line= list(map(int, input()))
        arr.append(line)
    dist =[[10000]*N for _ in range(N)]
    find_path(arr)
    print(f"#{test_case} {dist[-1][-1]}")