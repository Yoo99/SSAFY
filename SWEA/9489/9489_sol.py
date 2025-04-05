import sys
sys.stdin = open("9489_input.txt")
from collections import deque
# 상 하 좌 우만 확인하는 것

# 깊이 탐색
def depth(idx, idy):
    queue = deque([(idx,idy)])
    visited[idx][idy] = True
    cnt = 1
    while queue:
        x,y = queue.popleft()
        nx ,ny = x+1, y
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and maze[nx][ny]==1:
            cnt +=1
            visited[nx][ny] = True
            queue.append((nx,ny))
    return cnt
# 너비 탐색
def bfs(idx,idy):
    queue = deque([(idx,idy)])
    visited2[idx][idy] = True
    cnt = 1
    while queue:
        x,y = queue.popleft()
        nx,ny = x, y+1
        if 0<=nx<N and 0<=ny<M and not visited2[nx][ny] and maze[nx][ny]==1:
            cnt+=1
            visited2[nx][ny] = True
            queue.append((nx,ny))
    return cnt
T = int(input())
for test_case in range(1, T+1):
    N , M = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(N)]
    length = 0  # 총길이들의 집합
    # 세로 열의 총 길이 구하기
    visited = [[False] * M for _ in range(N)] # 세로 열의 총 길이 구하기
    visited2 = [[False] * M for _ in range(N)]
    for col in range(M):
        for row in range(N):
            if maze[row][col] == 1 and not visited[row][col]:
                d = depth(row, col)
                if d>length:
                    length = d
                else:
                    continue
    for row in range(N):
        for col in range(M):
            if maze[row][col] == 1 and not visited2[row][col]:
                d = bfs(row,col)
                if d>length:
                    length =d
                else:
                    continue
    print(f"#{test_case} {length}")