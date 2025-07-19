import sys
sys.stdin = open("04.dijkstra_input.txt")
import heapq

direction = [(-1, 0), (0, -1), (1,0), (0,1)] #상하좌우 방향

def find_path(dx,dy):
    global dist, arr
    hq = [(arr[dx][dy],0,dx, dy)]
    while hq:
        val,w,x,y = heapq.heappop(hq) # arr에서 해당 위치의 값, x좌표, y좌표
        for cx, cy in direction:
            nx,ny = cx + x, cy+y
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]<val: # 낮은 곳으로 이동하는 경우
                    if dist[nx][ny]<=w:
                        continue
                    dist[nx][ny] = w
                    heapq.heappush(hq,(arr[nx][ny],w,nx,ny))
                elif arr[nx][ny]> val: # 높은 곳으로 이동하는 경우
                    new_dist = 2*(abs(arr[nx][ny]) - val) + w
                    if dist[nx][ny]<new_dist:
                        continue
                    dist[nx][ny] = new_dist
                    heapq.heappush(hq, (arr[nx][ny], new_dist,nx,ny))
                elif arr[nx][ny] ==val:
                    new_dist = 1+w
                    if dist[nx][ny]<new_dist:
                        continue
                    dist[nx][ny] = new_dist
                    heapq.heappush(hq, (arr[nx][ny], new_dist, nx,ny))
            if nx == N - 1 and ny == N - 1:
                break
    return dist[-1][-1]

T = int(input()) # test_case의 개수
for test_case in range(1, T+1):
    N = int(input()) # 한변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    print(f"#{test_case} {find_path(0,0)}")
