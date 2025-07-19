import sys
sys.stdin = open("5656_input.txt")
from collections import deque
import copy

direction = [(-1,0), (0, -1), (1,0), (0,1)] # 상하좌우 4가지 방향
def gravity(W, H, arr): # 중력을 적용할 수 있는 문제
    for col in range(W):
        stack = []
        for row in range(H-1,-1,-1):
            if arr[row][col]>0:
                stack.append(arr[row][col])
                arr[row][col] = 0
            else:continue
        for idx in range(len(stack)):
            arr[H-1-idx][col] = stack[idx]
    return arr

def find_col(W, H, arr,depth =0):
    global N, min_count
    if depth == N:
        cnt = 0
        for row in arr:
            for ele in row:
                if ele >0:
                    cnt +=1
        if cnt <min_count:
            min_count = cnt
        return min_count
    for col in range(W):
        temp = copy.deepcopy(arr)
        cnt = 0 # 총 깬 벽돌의 개수를 저장하기 위한 변수
        for row in range(H):
            if temp[row][col]>0:
                queue = deque([(row, col, temp[row][col])])
                temp[row][col]  = 0
                break
        else:
            continue
        while queue:
            x,y,power = queue.popleft() # x좌표,y좌표, power
            temp[x][y] = 0
            cnt +=1
            for d in range(4):
                for i in range(1, power):
                    nx,ny = x + direction[d][0]*i, y+direction[d][1]*i
                    if 0<=nx<H and 0<=ny<W and temp[nx][ny]>0:
                        queue.append((nx,ny, temp[nx][ny]))
                        temp[nx][ny] =0
                    else:
                        continue
        gravity(W, H, temp) #중력 적용
        find_col(W, H, temp, depth+1)
    return min_count
T = int(input()) # test case의 개수
for test_case in range(1, T+1):
    N, W, H = map(int, input().split()) # 구슬의 개수, 열의 개수, 행의 개수
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_count = float('inf') # 무한으로 두기
    d = find_col(W, H, arr, 0)
    if d == float('inf'):
        print(f"#{test_case} 0")
        continue
    else:
        print(f"#{test_case} {d}")
