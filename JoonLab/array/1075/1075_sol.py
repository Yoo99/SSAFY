import sys
sys.stdin = open("input.txt")

N = int(input())
arr = []
for _ in range(N):
    line=  list(map(int, input().split()))
    arr.append(line)
i1, j1,i2,j2 ,k = map(int ,input().split())
for idx in range(i1, i2+1):
    for idy in range(j1, j2+1):
        arr[idx][idy] *= k
total = 0

for line in arr:
    total+= sum(line)
print(total)