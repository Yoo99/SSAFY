import sys
sys.stdin = open("1249_input.txt")
import heapq

direction = [(-1,0),(0,-1),(1,0),(0,1)]

def find_path(idx,idy):
    dist[idx][idy] = arr[idx][idy]
    hq = [(idx,idy)]
    while hq:
        x,y = heapq.heappop(hq)
        if x == N-1 and y == N-1:
            break
        for dx, dy in direction:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                new_dist = dist[x][y] + arr[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(hq,(nx,ny))

    return dist[-1][-1]



T = int(input()) # 테스트 케이스의 개수
for test_case in range(1, T+1):
    N = int(input()) # 한 변의 길이
    arr = []
    for _ in range(N):
        line = list(map(int ,input()))
        arr.append(line)
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    print(f"#{test_case} {find_path(0,0)}")
