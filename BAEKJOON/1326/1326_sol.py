import sys
sys.stdin = open("1326_input.txt")

_ = int(input())
rock = list(map(int, input().split()))
start, end = map(int, input().split())
start,end = start-1, end-1
cnt = 0
for i in range(start, end):
    cnt +=1
    dist = end - rock[i]
    if dist<rock[i]:
        print(-1)
        break
    dist = dist % rock[i]
    if dist ==0:
        print(cnt)
        break
