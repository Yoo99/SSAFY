import sys
sys.stdin = open("5656_input.txt")
from collections import deque

direction = [(-1,0), (0,-1), (1,0),(0,1)] # 상하좌우 방향 리스트 담기

T  = int(input()) # test case의 개수
# for test_case in range(1, T+1):
N , W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)] # 배열
# 제일 많이 적재되어 있는 열을 찾는다
for _ in range(N):
    cols = [] # 열마다 적재된 구슬의 총합을 저장할 리스트
    for col in range(W): # 열을 정하기
        col_sum = 0
        for row in range(H): # 모든 행을 다 더해야해
            col_sum += arr[row][col]
        cols.append(col_sum)
    # 제일 많이 쌓여 있는 열의 인덱스를 구하기
    # print("default arr", arr)
    max_index = cols.index(max(cols))
    for row in range(H):
        if arr[row][max_index] != 0:
            queue = deque([(row, max_index,arr[row][max_index])]) # 큐에다가 행, 열, 구슬의 힘의 크기를 저장
            while queue:
                x,y,power = queue.popleft()
                arr[x][y] = 0
                for d in range(4):
                    for i in range(power-1):
                        nx,ny = x + direction[d][0]*(i), y + direction[d][1]*(i)
                        # print(nx,ny)
                        if 0<=nx<W and 0<=ny<H and arr[nx][ny]!=0:
                            queue.append((nx,ny, arr[nx][ny]))
                            arr[nx][ny] = 0
                        else:
                            continue
    # 중력에 의한 효과를 주기
                for col in range(W):
                    for row in range(H-1):
                        if arr[row][col] !=0:
                            d = arr[row][col]
                            if arr[row+1][col] ==0:
                                arr[row+1][col] = d
                                arr[row][col] = 0
                            # else:
                            #     continue
for row in arr:
    print(*row)
