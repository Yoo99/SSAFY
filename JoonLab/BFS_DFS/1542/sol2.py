import heapq

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
maze = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

# 1~6 위치 추출
arrival = [None] * 6
for i in range(5):
    for j in range(5):
        if 1 <= maze[i][j] <= 6:
            arrival[maze[i][j] - 1] = (i, j)

def find_path(sx, sy, ex, ey):
    dist = [[float('inf')] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    hq = []
    heapq.heappush(hq, (0, sx, sy))
    dist[sx][sy] = 0

    while hq:
        d, x, y = heapq.heappop(hq)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if (x, y) == (ex, ey):
            return d

        # 일반 이동
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != -1 and not visited[nx][ny]:
                if dist[nx][ny] > d + 1:
                    dist[nx][ny] = d + 1
                    heapq.heappush(hq, (d + 1, nx, ny))

        # 슬라이딩 이동
        for dx, dy in direction:
            cx, cy = x, y
            while True:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < 5 and 0 <= ny < 5):
                    break
                if maze[nx][ny] == -1:
                    break
                cx, cy = nx, ny
                if maze[cx][cy] == 7:
                    break
            if not visited[cx][cy] and dist[cx][cy] > d + 1:
                dist[cx][cy] = d + 1
                heapq.heappush(hq, (d + 1, cx, cy))

    return -1

# 전체 이동 거리 계산
answer = 0
for target in arrival:
    d = find_path(r, c, *target)
    if d == -1:
        answer = -1
        break
    answer += d
    r, c = target

print(answer)