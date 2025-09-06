import sys
sys.stdin = open("input.txt")

directions=[(-1, 0), (0, -1), (1,0) ,(0, 1)]
maze = []
for _ in range(5):
    line=  list(map(int, input().split()))
    maze.append(line)
r,c = map(int, input().split())
visited = [[False for _ in range(5)] for _ in range(5)]
result = 0
def dfs(r, c, depth, cnt):
    global result, maze

    if depth>3:
        return

    if depth <=3 and cnt>=2:
        result = 1
        return
    x, y = r, c
    visited[x][y]=  True
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<= nx<5 and 0<=ny<5 and maze[nx][ny] != -1 and not visited[nx][ny]:
            dfs(nx,ny, depth+1, cnt+ maze[nx][ny])
    visited[x][y] = False
    return
dfs(r,c, 0,0)
print(result)
