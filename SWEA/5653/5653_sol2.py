import sys
sys.stdin = open("5653_input.txt")
import heapq

direction = [(-1,0),(0,-1),(1,0),(0,1)]

T = int(input())  # 테스트 케이스 개수
N, M, K = map(int, input().split())  # 세로 N, 가로 M, K 시간

arr = [[-1 for _ in range(M + 3*K)] for _ in range(N + 3*K)]
mid_x = (M + 3*K) // 2
mid_y = (N + 3*K) // 2

semi = []
for _ in range(N):
    line = list(map(int, input().split()))
    semi.append(line)

hq = []
for _ in range(N):
    for idx in range(mid_y, mid_y + N):
        arr[idx][mid_x: mid_x + M] = semi[idx - mid_y][:]

time = 0
for idx in range(M + 3*K):
    for idy in range(N + 3*K):
        if arr[idx][idy] > 0:
            heapq.heappush(hq, (time, arr[idx][idy], idx, idy))

while hq:
    time += 1
    d = len(hq)
    if time == K:
        break
    for _ in range(d):
        cnt, t, x, y = heapq.heappop(hq)
        if (cnt + t) > time:
            heapq.heappush(hq, (cnt, t, x, y))
            continue
        if t - 1 == 0:
            arr[x][y] = 0
        elif t - 1 > 0:
            heapq.heappush(hq, (time, t - 1, x, y))
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if arr[nx][ny] == -1:  # ✅ 수정 포인트!
                arr[nx][ny] = t
                heapq.heappush(hq, (time, t, nx, ny))

cnt = 0
for row in arr:
    for ele in row:
        if ele > 0:  # ✅ 선택적으로 더 깔끔하게
            cnt += 1
print(cnt)