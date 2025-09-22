import sys
sys.stdin = open("input.txt")

directions = [(-1, 0), (0, -1), (1,0), (0, 1)]
def find_apple(r,c, cnt, apple, maze):
    global answer
    if apple==3:
        answer = min(cnt, answer)
        return
    if cnt>=answer:
        return
    for dx, dy in directions:
        nx, ny = r + dx, c + dy
        if 0<=nx <5 and 0<=ny<5 and maze[nx][ny]!=-1:
            origin =maze[nx][ny]
            maze[nx][ny] = -1
            find_apple(nx,ny, cnt+1, apple+origin, maze)
            maze[nx][ny] = origin

maze = []
for _ in range(5):
    line = list(map(int, input().split()))
    maze.append(line)
answer = float('inf')
r,c  = map(int, input().split())
origin_start = maze[r][c]
maze[r][c] =-1
find_apple(r, c, 0, origin_start, maze)
maze[r][c] = origin_start
if answer == float('inf'):
    print(-1)
else:
    print(answer)