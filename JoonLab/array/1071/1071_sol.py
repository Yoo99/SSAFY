import sys
sys.stdin = open("input.txt")

n, k= map(int,input().split())
array = list(map(int, input().split()))
cnt = 0
for d in array:
    if d==k:
        cnt +=1
print(cnt)