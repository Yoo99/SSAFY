import sys
sys.stdin = open("1249_input.txt")
import heapq

direction = [(-1,0),(0,-1),(1,0),(0,1)]

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        line = list(map(int, input()))
        maze.append(line)
    dist = [[10000000000000] * N for _ in range(N)]
    dist[0][0] = maze[0][0]
    queue = [(dist[0][0],0,0)] # 비용, x좌표, y좌표
    while queue:
        cost, x,y = heapq.heappop(queue)
        for dx,dy in direction:
            nx,ny=  x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:
                new_cost = cost + maze[nx][ny]
                if new_cost<dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(queue, (dist[nx][ny], nx,ny))
    print(f"#{test_case} {dist[-1][-1]}")
