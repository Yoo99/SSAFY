import sys
sys.stdin = open("5656_input.txt")
from collections import deque

direction = [(-1, 0), (0, -1), (1, 0) ,(0,1)] # 상하좌우 방향

def gravity(W,H, arr):
    for col in range(W):
        for row in range(H-1, -1, -1): # 아래에서부터 위로 올라가면서 0이 있으면 밑으로 끌어내리기
            if arr[row][col] == 0:
                if arr[row-1][col]>0:
                    arr[row][col] = arr[row-1][col]
                    arr[row-1][col] = 0
            else:
                continue
    return arr

T = int(input()) # test case의 개수
N , W, H = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(H)]
for _ in range(N):
    cols_sum = [] #
    for idy in range(W): # 모든 열마다 실행해보기 위한 것
        cnt = 0
        arr2 = [] # 원본의 복제본 만들기
        for row in range(H):
            line=  arr[row][:]
            arr2.append(line)
        # 첫 폭파 지점 찾기
        for row in range(H):
            if arr2[row][idy]>0:
                queue = deque([(row, idy,arr2[row][idy])]) # x좌표,y좌표, power
                break
        while queue:
            x,y, power = queue.popleft()
            arr2[x][y] = 0
            cnt +=1
            for d in range(4):
                for i in range(1, power):
                    nx,ny = direction[d][0]*i + x, direction[d][1]*i
                    if 0<=nx<H and 0<=ny<W and arr2[nx][ny]>0:
                        queue.append((nx,ny, arr2[nx][ny]))
                        arr2[nx][ny] = 0
                    else:
                        continue
            gravity(W, H, arr2) # 중력에 의한 초기화 진행
        cols_sum.append(cnt)
    print(cnt)
    # 최대로 많이 벽돌이 깨지는 애를 찾아서 arr를 교체해주기
    max_col = cols_sum.index(max(cols_sum)) #가장 많이 깰 수 있는 칼럼 위치 확인
    print(max_col)
    # arr을 가장 많이 깰 수 있는 애로 초기화하는 중
    for row in range(H):
        if arr[row][max_col]>0:
            queue = deque([(row, max_col, arr[row][max_col])]) # x좌표,y 좌표, power
            break
    while queue:
        x,y,power = queue.popleft()
        arr[x][y] = 0
        for d in range(4):
            for i in range(1, power):
                nx,ny = direction[d][0]*i + x, direction[d][1]*i
                if 0<=nx<H and 0<=ny<W and arr[nx][ny]>0:
                    queue.append((nx,ny, arr[nx][ny]))
                    arr[nx][ny] = 0
                else:
                    continue
    gravity(W, H, arr)
for row in arr:
    print(*row)