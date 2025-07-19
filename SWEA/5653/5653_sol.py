import sys
sys.stdin = open("5653_input.txt")
import heapq

direction = [(-1,0),(0,-1),(1,0),(0,1)]

T = int(input()) # 테스트 케이스의 크기
N, M, K = map(int, input().split()) # 세로 N, 가로 M, K 시간
arr = [[-1 for _ in range(M + 3*K)] for _ in range(N + 3*K)]
# 가로의 중앙
mid_x = (M+3*K)//2
mid_y = (N+3*K)//2
semi = []
for _ in range(N):
    line=  list(map(int,input().split()))
    semi.append(line)
hq = []
for _ in range(N):
    for idx in range(mid_y, mid_y+N):
        arr[idx][mid_x: mid_x+M] = semi[idx-mid_y][:]
time = 0 # 시간이 흐르는 걸 표시하기 위해서
for idx in range(M+3*K):
    for idy in range(N+3*K):
        if arr[idx][idy] >0:
            heapq.heappush(hq, (time,arr[idx][idy], idx,idy))

# for row in arr:
#     print(row)

while hq:
    time +=1
    d = len(hq)
    if time == K:
        break
    print(time)
    for _ in range(d):
        cnt, t, x,y  = heapq.heappop(hq) # 큐에 넣었을 때 시간,
        if (cnt+t) > time: # 만약에 pop 된 애가 아직 활성화되지 않은 세포일 경우 다시 대입
            heapq.heappush(hq, (cnt, t, x,y))
            continue
        arr[x][y] = t-1
        if (t-1)>0:
            heapq.heappush(hq, (cnt-1, t-1, x,y))
        for dx, dy in direction:
            nx,ny = x+dx, y+dy
            if arr[nx][ny] !=0 and arr[nx][ny]==-1:
                arr[nx][ny] = t
                heapq.heappush(hq, (time, t, nx,ny))

cnt = 0
for row in arr:
    print(row)
# for row in arr:
#     for ele in row:
#         if ele>0:
#             cnt +=1
# print(cnt)


