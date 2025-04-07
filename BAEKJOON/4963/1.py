import sys
from collections import deque
sys.stdin = open("4963_input.txt")
input = sys.stdin.readline
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
result = []

while True:
    line = input()
    if not line.strip():
        continue  # 빈 줄 무시

    w, h = map(int, line.strip().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    island = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                queue = deque([(i, j)])
                arr[i][j] = 0

                while queue:
                    print(queue)
                    x, y = queue.popleft()

                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                            arr[nx][ny] = 0
                            queue.append((nx, ny))
                island += 1

    result.append(island)

for i in result:
    print(i)