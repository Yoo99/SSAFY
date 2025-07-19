import sys
import heapq
sys.stdin = open("input.txt")
directions = [(-1, 0), (0, -1), (1, 0), (0,1)]

arr = []
answer = 0
for _ in range(5):
    line = list(map(int, input().split()))
    arr.append(line)
dist = [[100000 for _ in range(5)] for _ in range(5)] # 거리를 기록하는 곳
sr, sc = map(int ,input().split()) # 지정된 출발점
dist[sr][sc] = 0

def find_path(sr,sc, arr, dist, tr,tc):
    hq = [] # 힙큐
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[sr][sc] = True
    heapq.heappush(hq, (dist[sr][sc], sr, sc))
    while hq:
        distance, x,y = heapq.heappop(hq)
        if x==tr and y == tc:
            return arr[x][y]
        for dx, dy in directions:
            nx,ny = x + dx , y + dy
            if 0<=nx<5 and 0<=ny<5 and arr[nx][ny] != -1 and not visited[nx][ny] :
                dist[nx][ny] = distance + 1
                visited[nx][ny] = True
                heapq.heappush(hq, (dist[nx][ny], nx,ny))
            else:
                continue
    return -1

dest = []
for num in range(1, 7):
    for idx in range(5):
        for idy in  range(5):
            if arr[idx][idy] == num:
                dest.append((idx,idy))
for i in range(len(dest)):
    tr,tc = dest[i]
    d = find_path(sr,sc, arr, dist, tr,tc)
    if d == (i+1):
        sr,sc = tr, tc
        answer = dist[tr][tc]
    else:
        answer = -1
        break
print(answer)