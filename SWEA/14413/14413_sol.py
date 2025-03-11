import sys
sys.stdin = open("14413_input.txt")
from collections import deque
direction = [(-1,0), (0,-1),(1,0),(0,1)]

T = int(input())
for test_case in range(1, T+1):
    N,M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = list(input())
        arr.append(line)
    # 우선 ? 채우기
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] =='?':
                queue.append((i,j))
    flag = True
    while queue:
        i,j=  queue.popleft()
        subset = []
        for dx, dy in direction:
            nx, ny= dx+i, dy+j
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] !='?':
                subset.append(arr[nx][ny])
        if len(set(subset)) ==1:
            if subset[0] =='.':
                arr[i][j] = '#'
            else:
                arr[i][j] = '.'
        elif len(subset)==0:
            queue.append((i,j))
        else:
            flag = False
            break

    if any('?' in row for row in arr):
        print(f"#{test_case} impossible")
        continue

    find_flag = True
    while find_flag:
        for row in range(N):
            for col in range(M):
                d = arr[row][col]
                for dx, dy in direction:
                    nx,ny=  row+dx, col + dy
                    if 0<=nx<N and 0<=ny<M:
                        if arr[nx][ny] == d:
                            find_flag = False
                        else:
                            continue
        if row ==N-1 and col ==M-1:
            break
    if find_flag:
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")



