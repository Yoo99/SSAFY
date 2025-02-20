import sys
from collections import deque
sys.stdin = open("5656_input.txt")

direction = [(-1,0),(0,-1),(1,0),(0,1)]

def default_mode(arr):
    for col in range(W):
        for row in range(H):



T = int(input()) # 테스트 케이스의 개수
N, W, H = map(int, input().split()) # 구슬 N개, 가로(열의 개수 - W), 세로 (row의 개수 - H)
# 벽돌 배열
arr = []
for i in range(H):
    line=  list(map(int, input().split()))
    arr.append(line)

for j in range(N): # 구슬의 개수만큼
    # 최대 벽돌이 있는 col의 idx를 확인한다
    col_idx = []
    for col in range(W):
        cnt= 0
        for row in range(H):
            cnt += arr[row][col]
        col_idx.append(cnt)
    max_idx = col_idx.index(max(col_idx))
    # 가장 많은 벽돌이 존재하는 col의 인덱스
    # row 인덱스를 확인하기
    for row in range(H):
        if arr[row][max_idx] > 0:
            start_row = row
    queue = deque([(start_row, max_idx, arr[row][max_idx])])
    while queue:
        x,y, val = queue.popleft()
        for num in range(val):
            for dx, dy in direction:
                nx, ny = x + dx*num, y+dy*num
                if 0<=nx<H and 0<=ny<W and arr[nx][ny]>0:
                    queue.append((nx,ny, arr[nx][ny]))
                    arr[nx][ny] = 0
                # 벽돌 초기화
