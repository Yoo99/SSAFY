import sys
sys.stdin = open("input.txt")

n, k = map(int,input().split()) # 차원, 비교 숫자
cnt = 0
for _ in range(n):
    line = list(map(int, input().split()))
    for b in line:
        if b ==k:
            cnt+=1
print(cnt)

