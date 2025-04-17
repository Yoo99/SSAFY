import sys
sys.stdin = open("4193_input.txt")
import heapq

direction = [(-1,0), (0, 1), (1, 0), (0,-1)]

def find_path(start_x, start_y, dist = 0):
    global time
    global end_x, end_y
    hq = [(dist,start_x, start_y)] # 마지막에 있는 w의 경우에는 time에 해당
    while hq: # queue가 존재할 때
        w, x, y = heapq.heappop(hq) # q에 들어있던 x 좌표와 y 좌표 추출
        if x==end_x and y == end_y:
            break
        for dx, dy in direction:
            nx, ny=  dx+x, dy+y
            # maze가 2가 아닐 때
            if 0<=nx<N and 0<=ny<N and maze[nx][ny]!= 1 and maze[nx][ny]!=2:
                new_dist = w+1
                if maze2[nx][ny]<new_dist:
                    continue
                else:
                    maze2[nx][ny] = new_dist
                    heapq.heappush(hq, (new_dist,nx,ny))
            # maze[nx][ny]=2 일 때,
            if 0<=nx<N and 0<=ny<N and maze[nx][ny] == 2:
                if (w+1)%3 ==0: # 폭풍우를 지나갈 수 있을 때
                    new_dist = w+1
                    if maze2[nx][ny] < new_dist:
                        continue
                    else:
                        maze2[nx][ny] = new_dist
                        heapq.heappush(hq, (new_dist, nx,ny))
                else:
                    heapq.heappush(hq, (w+1,x,y))


    return maze2


T = int(input()) # test case의 개수
for test_case in range(1, T+1):
    N = int(input()) # 수영장의 가로 세로 크기
    maze = [list(map(int, input().split())) for _ in range(N)]
    maze2 = [[float('inf') for _ in range(N)] for _ in range(N)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    time = 0
    maze2[start_x][start_y] = 0
    find_path(start_x, start_y,0)
    if maze2[end_x][end_y] == float('inf'):
        print(f"#{test_case} {-1}")
        continue
    print(f"#{test_case} {maze2[end_x][end_y]}")
