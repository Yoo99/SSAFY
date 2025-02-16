import sys
from collections import deque
sys.stdin = open("5656_input", "r")
T = int(input())
direction = [(-1, 0), (0, -1), (1,0), (0,1)]
N, W, H = map(int,input().split())
print(N,W,H)
arr = []
for row in range(H):
    line= list(map(int ,input().split()))
    arr.append(line)
# 최상위 col_idx 구하기
for loop in range(N):
    # print("Throw", i)
    col_idx = []
    for col in range(W):
        line = []
        for row in range(H):
            line.append(arr[row][col])
        cnt = 0
        for ele in line:
            if ele>0:
                cnt +=ele
        col_idx.append(cnt)
    start_col = 0
    for i in range(0, len(col_idx)):
        if col_idx[i] == max(col_idx):
            start_col = i
    # 시작 위치 row_idx, max_idx 구하기
    start_row = 0
    for row_idx in range(H):
        if arr[row_idx][start_col] >0:
            start_row = row_idx
    queue = deque([(start_row,start_col, arr[start_row][start_col])])
    while queue:
        start_row,start_col, val = queue.popleft()
        arr[start_row][start_col] = 0
        for num in range(1,val):
            if 0<=start_row-num<H and 0<=start_col<W:
                if arr[start_row - num][start_col] >0:
                    queue.append((start_row-num, start_col, arr[start_row-num][start_col]))
                arr[start_row-num][start_col] = 0
            if 0<=start_row+num<H and 0<=start_col<W:
                if arr[start_row+num][start_col] >0:
                    queue.append((start_row+num, start_col, arr[start_row+num][start_col]))
                arr[start_row+num][start_col] = 0
            if 0<=start_row<H and 0<=start_col-num<W:
                if arr[start_row][start_col - num]>0:
                    queue.append((start_row, start_col-num, arr[start_row][start_col-num]))
                arr[start_row][start_col-num] = 0
            if 0<=start_row<H and 0<=start_col + num <W:
                if arr[start_row][start_col + num] >0:
                    queue.append((start_row, start_col+num, arr[start_row][start_col+num]))
                arr[start_row][start_col+num] =0

        # 벽돌 초기화
        # print(arr)
        line_list = []
        for col in range(W):
            line = []
            for row in range(H):
                if arr[row][col]>0:
                    line.append(arr[row][col])
            if len(line)<H:
                sub = [0 for _ in range(H-len(line))]
            sub = sub + line
            line_list.append(sub)
        # for line in line_list:
        #     print(line)
        # print()
        for col in range(W):
            for row in range(H):
                arr[row][col] = line_list[col][row]
#
sum = 0
for row in range(H):
    for col in range(W):
        sum += arr[row][col]
print(sum)

