import sys
sys.stdin = open("1600_input.txt")
from collections import deque

direction = [(-1, 0),(0,-1),(1,0),(0,1)] # 방향
jump_horse = [(1,-2),(2,-1),(-1,-2),(-2,-1),(2,1),(1,2),(-1,2),(-2,1)]

def find_path(idx,idy):
    global zoo, N,M,K, visited
    q = deque([(idx,idy, 0,0)])
    visited[0][0][0] = True
    while q:
        x,y,jump, cnt = q.popleft()
        if x ==M-1 and y==N-1:
            return cnt
        for dx, dy in direction:
            nx,ny = x+dx, y+ dy
            if 0<=nx<M and 0<=ny<N:
                if not visited[nx][ny][jump] and zoo[nx][ny] ==0:
                    visited[nx][ny][jump] = True
                    q.append((nx,ny, jump,cnt+1))
        if jump<K:
            for dx,dy in jump_horse:
                nx,ny = x+dx, y+dy
                if 0<=nx<M and 0<=ny<N:
                    if not visited[nx][ny][jump+1] and zoo[nx][ny]==0:
                        visited[nx][ny][jump+1] = True
                        q.append((nx,ny, jump+1, cnt+1))
    return -1

K = int(input()) # 동작수의 최솟값
N, M = map(int, input().split()) # 열 ,행
zoo = [list(map(int, input().split())) for _ in range(M)]
visited = [[[False for _ in range(K+1)] for _ in range(N)] for _ in range(M)]
print(find_path(0,0))