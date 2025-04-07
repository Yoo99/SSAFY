import sys
sys.stdin = open("4963_input.txt")
from collections import deque
direction = [(-1,-1), (-1,0),(-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]

input = sys.stdin.readline
result =[]
while True:
    line = input()
    if not line.strip():
        continue
    w, h = map(int, line.strip().split())
    if w==0 and h==0:
        break
    arr=[list(map(int, input().split())) for _ in range(h)]
    # 배열을 입력 받는 부분
    island = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                queue = deque([(i,j)])
                cnt = 0
                while queue:
                    print(queue)
                    x,y = queue.popleft()
                    arr[x][y] = 0
                    cnt +=1
                    for dx,dy in direction:
                        nx,ny=  x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and arr[nx][ny]==1:
                            queue.append((nx,ny))

                island+=1

    result.append(island)
for i in result:
    print(i)