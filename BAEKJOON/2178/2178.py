import sys
sys.stdin = open("2178_input.txt", "r")

direction = [(-1,0), (0, -1), (0,1), (1,0)]
def dfs(idx, idy):
    if


for test_case in range(4):
    N, M  = map(int, input().split())
    arr= []
    visited = [[False] * N for _ in range(M)]
    for i in range(N):
        line= list(map(int, input()))
        arr.append(line)
    print(arr)
    cnt = 0
    for row in range(0,N):
        for col in range(0,M):
            visited[row][col] = True
            cnt +=1
            for dx, dy in direction:
                nx = dx + row; ny = dy+col
                if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1 and visited[nx][ny] == False:
                    print(nx,ny)
                    visited[nx][ny] = True
                    cnt +=1
                    if nx ==N and ny == M:
                        break
    print(cnt)