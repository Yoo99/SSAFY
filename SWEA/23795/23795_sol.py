import sys
sys.stdin = open("23795_input.txt")
#               좌      상       우     하
direction = [(-1, 0), (0, 1), (1,0),(0,-1)]

def find_direciton(idx,idy, arr, N):
    for dx, dy in direction:
        nx , ny = idx + dx , idy + dy
        while 0<=nx<N and 0<=ny<N and arr[nx][ny]==0:
            arr[nx][ny] = 3
            nx, ny = nx + dx, ny +dy
    return arr


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        line = list(map(int ,input().split()))
        arr.append(line)
    idx,idy = 0,0
    # 괴물의 위치 확인
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==2:
                idx ,idy = i,j
                break
    d = find_direciton(idx,idy, arr, N)
    cnt = 0
    for row in d:
        e = row.count(0)
        cnt += e
    print(f"#{test_case} {cnt}")
