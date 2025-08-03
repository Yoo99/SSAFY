import sys
sys.stdin = open("input.txt")

N = int(input())
array=  list(map(int, input().split()))
k = int(input())
cnt  = 0
for a in array:
    if a ==k:
        cnt +=1
print(cnt)