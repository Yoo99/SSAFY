import sys
sys.stdin = open("1824_input.txt")
from collections import deque
              # 우   좌         하       상
direction = [(0, 1),(0,-1) , (1,0) , (-1,0) ]

def move(x,y,visited, memory):
    global answer
    visited[x][y] = True
    if memory[x][y] =='@':
        return "YES"
    queue = deque[(x,y)]
    while queue:
        x,y = queue.popleft()
        if arr[x][y] in ('<','>','^','.','_') and not visited[x][y]:  # 'v','|','?'
            if arr[x][y] == '<':
                nx ,ny = x, y-1
            elif arr[x][y] == '>':
                nx,ny = x, y+1
            elif arr[x][y] =='^':
                nx,ny = x-1, y
            elif arr[x][y] == 'v':
                nx,ny = x+1 ,y
            elif arr[x][y] == '.':
                nx,ny = x, y+1
            elif arr[x][y] == '_':
                if memory[x][y] == 0:
                    nx,ny = x, y+1
                else:
                    nx,ny = x, y-1
            if nx>=R:
                nx -= R
            elif nx<0:
                nx += R
            if ny >=C:
                ny -= C
            elif ny <0:
                ny +=C

        #     if ny>=C: ny = ny-C
        #     if ny<0: ny= C-1
        #     if not visited[nx][ny]:
        #         move(nx,ny, visited,memory)
        #     else:
        #         return "No"
        # if memory[x][y] =='>':
        #     nx,ny = x,y+1
        #     if ny>=C: ny = ny-C






T = int(input())
# for test_case in range(1, T+1):
R,C = map(int, input().split())
arr = []
for _ in range(R):
    line = list(input())
    arr.append(line)
for row in arr:
    print(row)
memory = [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
