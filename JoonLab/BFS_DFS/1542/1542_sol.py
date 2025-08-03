import sys
sys.stdin = open("input.txt")

import heapq
direction = [(-1, 0), (0,-1),(1,0),(0,1)]
maze = []
for _ in range(5):
    line=  list(map(int,input().split()))
    maze.append(line)
r,c = map(int,input().split())

arrival = [[] for _ in range(6)]
for num in range(1, 7):
    for idx in range(5):
        for idy in range(5):
            if maze[idx][idy] == num:
                arrival[num-1] = [idx,idy]

def find_path(x,y, maze,idx,idy):
    dist = [[float('inf') for _ in range(5)] for _ in range(5)]
    visited = [[False for _ in range(5)] for _ in range(5)]
    hq = []
    dist[x][y] = 0
    visited[x][y] = True
    heapq.heappush(hq, (dist[x][y], x,y))
    while hq:
        distance, x,y = heapq.heappop(hq)
        if x == idx and y == idy:
            # dist[x][y]  =distance+1
            return dist[idx][idy], dist
        for dx, dy in direction:
            nx,ny = x+dx , y + dy
            if 0<=nx<5 and 0<=ny<5 and maze[nx][ny]!=-1 and not visited[nx][ny]:
                newdist = distance+1
                dist[nx][ny] = min(dist[nx][ny], newdist)
                visited[nx][ny] = True
                heapq.heappush(hq, (dist[nx][ny],nx,ny))
            else:
                break
        for dx, dy in direction:
            cx,cy = x,y
            while True:
                nx,ny = cx+dx, cy +dy
                if 0<=nx<5 and 0<=ny<5 and maze[nx][ny] !=-1:
                    cx,cy = nx,ny
                    if maze[nx][ny] ==7:
                        dist[nx][ny] = min(dist[nx][ny] ,distance) +1
                        heapq.heappush(hq, (dist[nx][ny],nx,ny))
                        break
                    # elif maze[nx][ny]==0:
                    #     dist[nx][ny] = distance
                    else:
                        dist[nx][ny] = distance
                else:
                    break
            if not visited[cx][cy]:
                dist[cx][cy] = min(dist[cx][cy], distance)
                heapq.heappush(hq, (dist[cx][cy],cx,cy))
                visited[cx][cy] = True


    return -1,dist

answer = 0

for number in range(len(arrival)):
    idx,idy = arrival[number]
    d,dist = find_path(r,c,maze, idx,idy)
    print(d)
    for line in dist:
        print(line)
    if d==-1:
        answer = -1
        break
    else:
        r,c = idx,idy
        answer += d
print(answer)
