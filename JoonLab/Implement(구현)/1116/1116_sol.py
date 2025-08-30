import sys
sys.stdin = open("input.txt")

from collections import deque
directions=[(-1, 0), (0, -1), (1,0) ,(0, 1)]

def solution(r,c):
    answer = 0
    global maze
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = deque([(r, c, 0, maze[r][c])])
    while q:
        x,y, depth, count = q.popleft()
        visited[x][y] = True
        if count >=2:
            answer =1
            return answer
        if depth >=3:
            continue
        for nx, ny in directions:
            cx, cy = nx +x , ny + y
            if 0<=cx<5 and 0<=cy<5 and not visited[cx][cy] and maze[cx][cy] != -1:
                count += maze[cx][cy]
                depth +=1
                q.append((cx,cy, depth, count))
            else:
                continue
    return answer
maze = []
for _ in range(5):
    line=  list(map(int, input().split()))
    maze.append(line)
r,c = map(int, input().split())
print(solution(r,c))