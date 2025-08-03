import sys
sys.stdin = open("input.txt")

arr = []
for _ in range(5):
    line=  list(map(int, input().split()))
    arr.append(line)
r,c = map(int, input().split())


ans = 0
directions = [(-1, 0), (0, -1), (1, 0), (0,1)]
for dx, dy in directions:
    nx,ny = r+dx, c+dy
    if 0<=nx<5 and 0<=ny<5 and arr[nx][ny] == 1:
        ans = 1
        break
print(ans)