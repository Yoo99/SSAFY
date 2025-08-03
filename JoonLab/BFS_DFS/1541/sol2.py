import sys
from collections import deque

sys.stdin = open("input.txt")
maze = []
direction = [(-1,0), (0,-1), (1,0), (0,1)]

# 미로 입력
for _ in range(5):
    maze.append(list(map(int, input().split())))

# 시작 위치 입력
r, c = map(int, input().split())

# 방문 여부 및 거리 초기화
visited = [[False] * 5 for _ in range(5)]
dist = [[10000] * 5 for _ in range(5)]

def find_path(maze, r, c, visited, dist):
    q = deque()
    dist[r][c] = 0
    visited[r][c] = True
    q.append((r, c))

    while q:
        x, y = q.popleft()

        # 목표 지점에 도달하면 거리 반환
        if maze[x][y] == 1:
            return dist[x][y]

        # 일반 상하좌우 이동
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != -1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # 미끄럼 이동
        for dx, dy in direction:
            cx, cy = x, y
            while True:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != -1:
                    if maze[nx][ny] == 7:  # 미끄럼 중단 지점
                        break
                    cx, cy = nx, ny
                else:
                    break
            # 미끄러진 끝 위치가 방문 안 되었을 경우만 큐 삽입
            if not visited[cx][cy]:
                visited[cx][cy] = True
                dist[cx][cy] = dist[x][y] + 1
                q.append((cx, cy))

    return -1  # 도달 불가

# 결과 출력
print(find_path(maze, r, c, visited, dist))
for line in dist:
    print(line)