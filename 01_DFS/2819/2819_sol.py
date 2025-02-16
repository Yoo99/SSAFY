import sys
from itertools import combinations_with_replacement
sys.stdin = open("input.txt")

direction = [(-1,0), (0,1),(0,-1),(1,0)]

def dfs(idx, idy, depth, path):
    if depth ==7:
        result.add(tuple(path))
        return
    for dx, dy in direction:
        nx ,ny = idx + dx, idy + dy
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx, ny, depth+1, path + [arr[nx][ny]])


T=  int(input())
for test_case in range(1, T+1):
    arr=[list(map(int, input().split())) for _ in range(4)]
    # print(arr)
    result = set()
    for row in range(4):
        for col in range(4):
            dfs(row, col, 1, [arr[row][col]])
    print(f"#{test_case} {len(result)}")
