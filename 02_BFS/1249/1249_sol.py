import sys
from collections import deque
sys.stdin = open("1249_input.txt","r")

direction = [(-1,0), (0,1), (1,0), (0,-1)]

def find_path(arr):
    queue = deque([(0,0)])
    distances[0][0] = arr[0][0]
    while queue:
        x, y= queue.popleft()
        cost = distances[x][y]
        for dx, dy in direction:
            nx = x + dx ; ny = y +dy
            if 0<=nx<N and 0<=ny<N:
                new_cost = cost + arr[nx][ny]
                if new_cost<distances[nx][ny]:
                    distances[nx][ny] = new_cost
                    queue.append((nx,ny))
    return distances[N-1][N-1]

tc = int(input())
for test_case in range(1, tc+1):
    N = int(input())
    arr = []
    for i in range(N):
        line = list(map(int, input()))
        arr.append(line)
    distances = [[100000] * N for _ in range(N)]
    print(f"#{test_case} {find_path(arr)}")