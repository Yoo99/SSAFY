import sys
sys.stdin = open("2819_input.txt","r")

N = int(input())
for test_case in range(1, N+1):
    arr = []
    for i in range(4):
        line = list(input().split())
        arr.append(line)
    print(arr)
    def dfs_grid(grid, x,y, depth, max_depth):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        if depth> max_depth:
            # print(line)
            return
        line.append(grid[x][y])
        for dx, dy in directions:
            nx, ny = x +dx, y+dy
            if 0<=nx<4 and 0<=ny<4:
                dfs_grid(grid, nx, ny, depth+1, max_depth)
    dfs_grid(arr,0,0,0,6)
    print(len(line)//6)