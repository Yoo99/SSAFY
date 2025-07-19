import sys
sys.stdin = open("04.dijkstra_input.txt")
import heapq

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 상하좌우 방향 확인

def find_path(idx,idy):
    global dist, maze, N
    hq = [(dist[idx][idy],maze[idx][idy], idx,idy)]# w, val, x, y
    while hq:
        w, val, x,y = heapq.heappop(hq)
        for dx, dy in direction:
            nx,ny=  dx+x, dy+y
            if 0<=nx<N and 0<=ny<N: # 범위 안에 있다는 전제
                if maze[nx][ny] < val : # 이전 위치 값보다 높이가 낮은 경우
                    new_dist = w
                    if dist[nx][ny] <new_dist:
                        continue
                    else:
                        dist[nx][ny] = w
                        heapq.heappush(hq, (new_dist, maze[nx][ny], nx,ny))
                elif maze[nx][ny] == val : # 이전 위치와 높이가 동일한 경우
                    new_dist = w+1
                    if dist[nx][ny] < new_dist:
                        continue
                    else:
                        dist[nx][ny] = new_dist
                        heapq.heappush(hq, (new_dist, maze[nx][ny], nx,ny))
                elif maze[nx][ny] > val : # 이전 위치보다 높이가 높은 경우
                    new_dist = w + 2*(abs(maze[nx][ny]-val))
                    if dist[nx][ny] < new_dist:
                        continue
                    else:
                        dist[nx][ny] = new_dist
                        heapq.heappush(hq, (new_dist, maze[nx][ny], nx,ny))
    return dist[-1][-1]

T = int(input()) # test_case 의 개수
for test_case in range(1, T+1):
    N = int(input()) # 한 변의 길이
    maze = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    print(f"#{test_case} {find_path(0,0)}")